#!/usr/bin/env python3

import os
import sys
import socket
import subprocess
import hashlib
import ssl
import json
import time
import platform
import threading
import queue
from datetime import datetime
from urllib.request import Request, urlopen


VERSION = "2.0"


# ==========================
# Utility
# ==========================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def slow_print(text, delay=0.002):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()


def banner():

    art = f"""
   ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗
   ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║
   ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║
   ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║
   ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝
   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝

             ShadowMap Security Toolkit v{VERSION}
    """

    slow_print(art)


def log_event(message):

    os.makedirs("logs", exist_ok=True)

    with open("logs/shadowmap.log", "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")


def safe_input(prompt, limit=200):

    value = input(prompt).strip()

    if len(value) > limit:
        raise ValueError("Input too long")

    return value


# ==========================
# Spinner animation
# ==========================

def spinner(msg, duration=2):

    chars = "|/-\\"

    end = time.time() + duration
    i = 0

    while time.time() < end:
        sys.stdout.write(f"\r{msg} {chars[i % len(chars)]}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1

    print()


# ==========================
# DNS tools
# ==========================

def dns_lookup():

    domain = safe_input("Domain: ")

    spinner("Resolving")

    try:
        ip = socket.gethostbyname(domain)
        print("IP:", ip)

        log_event(f"dns {domain} -> {ip}")

    except:
        print("Lookup failed")


def reverse_dns():

    ip = safe_input("IP: ")

    try:

        host = socket.gethostbyaddr(ip)
        print("Hostname:", host[0])

        log_event(f"reverse dns {ip}")

    except:
        print("Reverse lookup failed")


# ==========================
# Whois
# ==========================

def whois_lookup():

    domain = safe_input("Domain: ")

    spinner("Querying whois")

    subprocess.run(["whois", domain])


# ==========================
# HTTP Header Inspection
# ==========================

def http_headers():

    url = safe_input("URL: ")

    if not url.startswith("http"):
        url = "http://" + url

    try:

        req = Request(url, method="HEAD")

        with urlopen(req) as response:

            headers = response.headers

            for h in headers:
                print(f"{h}: {headers[h]}")

        log_event(f"http header {url}")

    except Exception as e:

        print("Request failed:", e)


# ==========================
# SSL inspection
# ==========================

def ssl_info():

    domain = safe_input("Domain: ")

    ctx = ssl.create_default_context()

    try:

        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:

            s.connect((domain, 443))

            cert = s.getpeercert()

        print(json.dumps(cert, indent=2))

    except:

        print("SSL check failed")


# ==========================
# Port scanner
# ==========================

def scan_port(host, port, results):

    s = socket.socket()

    s.settimeout(1)

    try:

        s.connect((host, port))
        results.append(port)

    except:
        pass

    s.close()


def port_scan():

    host = safe_input("Host: ")

    start = int(safe_input("Start port: "))
    end = int(safe_input("End port: "))

    print("Scanning ports...")

    open_ports = []

    threads = []

    for port in range(start, end + 1):

        t = threading.Thread(target=scan_port, args=(host, port, open_ports))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    if open_ports:
        print("Open ports:", open_ports)
    else:
        print("No open ports found")


# ==========================
# Nmap wrapper
# ==========================

def nmap_scan():

    target = safe_input("Target: ")

    spinner("Running nmap", 3)

    subprocess.run(["nmap", "-sV", "-T4", target])


# ==========================
# Banner grabbing
# ==========================

def banner_grab():

    host = safe_input("Host: ")
    port = int(safe_input("Port: "))

    s = socket.socket()
    s.settimeout(3)

    try:

        s.connect((host, port))

        data = s.recv(1024)

        print("Banner:", data.decode(errors="ignore"))

    except:

        print("No banner")

    finally:

        s.close()


# ==========================
# Subdomain wordlist
# ==========================

COMMON_SUBS = [
    "www","mail","ftp","dev","api","test","beta","staging"
]


def subdomain_scan():

    domain = safe_input("Domain: ")

    print("Scanning common subdomains...")

    found = []

    for sub in COMMON_SUBS:

        host = f"{sub}.{domain}"

        try:

            socket.gethostbyname(host)
            found.append(host)

        except:
            pass

    if found:

        print("Found:")

        for f in found:
            print(f)

    else:
        print("No subdomains found")


# ==========================
# Hash tools
# ==========================

def hash_file():

    path = safe_input("File path: ")

    if not os.path.exists(path):

        print("File not found")
        return

    sha = hashlib.sha256()
    md5 = hashlib.md5()

    with open(path,"rb") as f:

        while True:

            chunk = f.read(4096)

            if not chunk:
                break

            sha.update(chunk)
            md5.update(chunk)

    print("SHA256:", sha.hexdigest())
    print("MD5:", md5.hexdigest())


# ==========================
# Local network info
# ==========================

def local_info():

    print("System:", platform.system())
    print("Node:", platform.node())
    print("Release:", platform.release())
    print("Machine:", platform.machine())

    hostname = socket.gethostname()

    ip = socket.gethostbyname(hostname)

    print("Hostname:", hostname)
    print("Local IP:", ip)


# ==========================
# Ping
# ==========================

def ping():

    host = safe_input("Host: ")

    count = "4"

    if platform.system().lower() == "windows":
        cmd = ["ping","-n",count,host]
    else:
        cmd = ["ping","-c",count,host]

    subprocess.run(cmd)


# ==========================
# Menu
# ==========================

def menu():

    while True:

        print("""

1 DNS Lookup
2 Reverse DNS
3 Whois Lookup
4 HTTP Headers
5 SSL Certificate
6 Port Scan
7 Nmap Scan
8 Banner Grab
9 Subdomain Scan
10 File Hash
11 Local System Info
12 Ping Host

0 Exit

""")

        choice = safe_input("Select: ")

        if choice == "1":
            dns_lookup()

        elif choice == "2":
            reverse_dns()

        elif choice == "3":
            whois_lookup()

        elif choice == "4":
            http_headers()

        elif choice == "5":
            ssl_info()

        elif choice == "6":
            port_scan()

        elif choice == "7":
            nmap_scan()

        elif choice == "8":
            banner_grab()

        elif choice == "9":
            subdomain_scan()

        elif choice == "10":
            hash_file()

        elif choice == "11":
            local_info()

        elif choice == "12":
            ping()

        elif choice == "0":
            sys.exit()

        else:
            print("Invalid choice")

        input("\nPress ENTER")
        clear()
        banner()


# ==========================
# main
# ==========================

def main():

    clear()

    banner()

    log_event("shadowmap started")

    menu()


if __name__ == "__main__":

    main()
