# BLIND-SQL

Blind SQL Injection Scanner (BSQLI)
BSQLI is a powerful and user-friendly tool designed to detect Blind SQL Injection vulnerabilities in web applications. Built with Python, this tool allows security researchers, penetration testers, and developers to test URLs for potential Blind SQLi vulnerabilities using custom payloads. Whether you're testing a single URL or a list of URLs, BSQLI provides detailed results and saves vulnerable URLs for further analysis.

Features
Blind SQLi Detection: Detects time-based Blind SQL Injection vulnerabilities by analyzing response times.

Custom Payloads: Supports custom payloads from a file, allowing you to tailor the attack to your target.

Multi-URL Support: Scan a single URL or a list of URLs from a file.

Proxy Support: Route requests through a proxy for anonymity or debugging.

Verbose Mode: Get detailed output for each request, including response times and status codes.

Save Results: Export vulnerable URLs to a file for further investigation.

User-Agent Spoofing: Randomizes user-agent headers to avoid detection.

Installation
Clone the repository:

bash
Copy
git clone https://github.com/your-username/BSQLI.git
cd BSQLI
Install the required dependencies:

bash
Copy
pip install requests
Run the script:

bash
Copy
python bsqli.py
Usage
Input URL or URL List: Provide a single URL or a file containing a list of URLs to scan.

Payload File: Specify the path to a file containing SQL injection payloads (e.g., payloads/xor.txt).

Cookie (Optional): Include a cookie in the request if the target requires authentication.

Proxy (Optional): Route requests through a proxy (e.g., http://127.0.0.1:8080).

Verbose Mode: Enable verbose mode for detailed output.

Save Results: Save vulnerable URLs to a file for further analysis.

Example Payloads
Here’s an example of a payload file (payloads/xor.txt):

Copy
' OR SLEEP(10)--
" OR SLEEP(10)--
' OR SLEEP(10)#
" OR SLEEP(10)#
Screenshots
BSQLI Demo

Disclaimer
This tool is intended for educational and ethical testing purposes only. Use it only on systems you own or have explicit permission to test. The author is not responsible for any misuse or damage caused by this tool.

Contributing
Contributions are welcome! If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
HARZE12

GitHub: https://github.com/HARZE12

Tool Repository: https://github.com/HARZE12/BSQLI

Support
If you find this tool useful, consider giving it a ⭐ on GitHub! Your support helps me improve and maintain this project.

This description provides a clear overview of the tool, its features, and how to use it, while also including sections for installation, usage, and legal disclaimers. You can customize the placeholder links (e.g., screenshots, repository URL) as needed.
