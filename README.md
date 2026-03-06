# ShadowMap 2.0 - Elite Recon & Security Toolkit
<pre>
███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗
██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║
███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║
╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║
███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝
             ShadowMap v2.0
           Yonathanpy aka Witwizard
</pre>

---

## Overview
ShadowMap 2.0 is a **stealth network reconnaissance and security toolkit** designed for **penetration testers, red teamers, and elite security researchers**.  
It combines **passive and active scanning, deep protocol analysis, dark web crawling, and anonymity features** in a single advanced toolset.

---

## Features

| Module | Description | Mode |
|--------|------------|------|
| DNS Lookup | Resolve domains and map IPs | Passive |
| Reverse DNS | Trace hostnames from IPs | Passive |
| Whois | Domain ownership and registrar info | Passive |
| HTTP Header Inspection | Inspect server headers and response | Passive |
| SSL Info | Analyze certificates and encryption | Passive |
| Port Scan | Multi-threaded TCP port scanning | Active |
| Nmap Scan | Service detection & version enumeration | Active |
| Banner Grab | Identify service banners | Active |
| Subdomain Scan | Enumerates common subdomains | Passive |
| File Hashing | SHA256 & MD5 for file integrity | Utility |
| Local System Info | Hostname, IP, OS, Architecture | Utility |
| Ping Host | ICMP reachability check | Utility |
| Tor/Dark Web Crawl | Anonymous hidden service mapping | Anon |

---

## Toolchain & Instrumentation

| Tool | Purpose |
|------|--------|
| Python 3 | Core implementation |
| Nmap | Active scanning & service discovery |
| Whois | Domain registration analysis |
| SSL/TLS Libraries | Certificate inspection |
| socket | TCP/UDP networking |
| threading | Parallel scan operations |
| hashlib | File integrity checks |
| stem | Tor control & anonymity |
| BeautifulSoup | HTML/Dark Web parsing |
| curl/wget | Optional network fetches |
| netcat | Optional service probing |
| tcpdump | Optional packet capture |
| OpenSSL | Crypto & certificate analysis |

---

## Network Recon & Status

| Type | Status |
|------|-------|
| Open Ports | `Active` |
| Services | `Detected` |
| SSL Certificates | `Verified` |
| Subdomains | `Enumerated` |
| Passive Recon | `Complete` |
| Dark Web Crawl | `Tor Active` |

>  **Note:** All operations are logged locally. Unauthorized replication or modification of this toolkit is prohibited.

---

## Supported Geographies (Research/Recon)

| Region | Status |
|--------|-------|
| Russia | Explored |
| Ethiopia | Low-level analysis |
| Japan | Explored |
| China | Explored |
| Turkey | Explored |
| United States | Explored |
| Canada | Explored |
| Cyprus | Explored |
| Netherlands | Explored |
| Saudi Arabia | Explored |

---

## Installation

```bash
git clone https://github.com/yonathanpy/ShadowMap.git
cd ShadowMap
chmod +x shadowmap_2.0.py
pip3 install -r requirements.txt

---

## Usage

```bash
python3 shadowmap_2.0.py

| Mode    | Description                                      |
| ------- | ------------------------------------------------ |
| Passive | Passive reconnaissance: subdomains, headers, SSL |
| Active  | Active scanning: ports, banners, Nmap services   |
| Anon    | Tor/Dark Web crawling and full anonymity         |


Logging & Security

All operations are logged locally in logs/shadowmap.log

Unauthorized copying, modification, or replication is strictly prohibited

All activity is monitored; local audit trails and security checks are enabled

Reverse-engineering or attempts to modify the tool without permission may trigger internal logging mechanisms



| Type                        | Details                                          |
| --------------------------- | ------------------------------------------------ |
| MIT                         | Core framework                                   |
| All Rights Reserved         | Unauthorized use prohibited                      |
| Proprietary Modules         | ShadowMap Advanced Tools                         |
| Redistribution Prohibited   | Cloning, copying, or fork modification forbidden |
| Modification Prohibited     | Unauthorized edits forbidden                     |
| Derivative Works Prohibited | Reverse engineering or reuse forbidden           |
| Commercial Use              | Forbidden without permission                     |
| Observability               | Usage tracked locally                            |
| Logging                     | Full audit trails                                |
| Monitoring                  | Real-time security monitoring                    |


| Contact | Info                                                    |
| ------- | ------------------------------------------------------- |
| Email   | [Witwizard001@proton.me](mailto:Witwizard001@proton.me) |
| GitHub  | [yonathanpy](https://github.com/yonathanpy)             |
| Profile | ShadowMap 2.0 - Offensive Security Research             |
