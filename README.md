# Blind SQL Scanner (BSS)

![image](https://github.com/user-attachments/assets/1e1ecac1-7046-41fe-ba68-6205d394049b)




**BSS** is a powerful and user-friendly tool designed to detect Blind SQL Injection vulnerabilities in web applications. Built with Python, this tool allows security researchers, penetration testers, and developers to test URLs for potential Blind SQLi vulnerabilities using custom payloads. Whether you're testing a single URL or a list of URLs, BSS provides detailed results and saves vulnerable URLs for further analysis.

---

## Features

- **Blind SQLi Detection**: Detects time-based Blind SQL Injection vulnerabilities by analyzing response times.
- **Custom Payloads**: Supports custom payloads from a file, allowing you to tailor the attack to your target.
- **Multi-URL Support**: Scan a single URL or a list of URLs from a file.
- **Proxy Support**: Route requests through a proxy for anonymity or debugging.
- **Verbose Mode**: Get detailed output for each request, including response times and status codes.
- **Save Results**: Export vulnerable URLs to a file for further investigation.
- **User-Agent Spoofing**: Randomizes user-agent headers to avoid detection.

---

## Requirements
Python 3.x
Required Python libraries: requests, argparse (typically these come with Python, but make sure they are installed).





## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/HARZE12/BSS.git
   cd BSS
   pip install requests



