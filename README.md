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

1. Create a virtual environment (optional but recommended):

Environment Setup
To ensure the tool runs smoothly:
```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Clone the repository:
```
   git clone https://github.com/HARZE12/BSS-TOOL.git
   cd BSS-TOOL
   pip install requests
```

##Usage

3. To use
   
```
python3 BSS-TOOL.py

```

⚠️ Disclaimer: The content in this repository is for educational and informational purposes only; the authors hold no responsibility for misuse. Ensure proper authorization before use, act responsibly at your own risk, and comply with all legal and ethical guidelines. 
