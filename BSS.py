import os

import requests

import time

import concurrent.futures

import random



class Color:

    RED = '\033[91m'

    GREEN = '\033[92m'

    YELLOW = '\033[93m'

    BLUE = '\033[94m'

    PURPLE = '\033[95m'

    CYAN = '\033[96m'

    RESET = '\033[0m'



class BSS:

    USER_AGENTS = [

        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",

        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.1.2 Safari/537.36",

        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.70",

        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0",

        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",

        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0",

        "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",

        "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36",

    ]



    def __init__(self):

        self.vulnerabilities_found = 0

        self.total_tests = 0

        self.verbose = False  # Default to not verbose

        self.vulnerable_urls = []  # List to store vulnerable URLs

        self.proxies = None



    def get_random_user_agent(self):

        """Returns a random user-agent string from the list."""

        return random.choice(self.USER_AGENTS)



    def set_proxy(self, proxy):

        """Set the proxy for requests."""

        self.proxies = {

            'http': proxy,

            'https': proxy,

        }



    def perform_request(self, url, payload, cookie):

        """

        Perform a GET request with the given URL, payload, and cookie.

        Returns a tuple containing:

            - success (bool): True if the request was successful, False otherwise

            - url_with_payload (str): The URL with the payload appended

            - response_time (float): The time taken for the request to complete

            - status_code (int): The HTTP status code

            - error_message (str): The error message if the request failed, None otherwise

        """

        url_with_payload = f"{url}{payload}"

        start_time = time.time()



        headers = {

            'User-Agent': self.get_random_user_agent()

        }



        try:

            response = requests.get(url_with_payload, headers=headers, cookies={'cookie': cookie} if cookie else None, proxies=self.proxies)

            response.raise_for_status()

            response_time = time.time() - start_time

            success = True

            error_message = None

        except requests.exceptions.RequestException as e:

            response_time = time.time() - start_time

            success = False

            error_message = str(e)



        return success, url_with_payload, response_time, response.status_code if success else None, error_message



    def read_file(self, path):

        """Reads a file and returns a list of non-empty lines."""

        try:

            with open(path, 'r', encoding='utf-8') as file:

                return [line.strip() for line in file if line.strip()]

        except Exception as e:

            print(f"{Color.RED}Error reading file {path}: {e}{Color.RESET}")

            return []



    def save_vulnerable_urls(self, filename):

        """Save the list of vulnerable URLs to a file."""

        try:

            with open(filename, 'w', encoding='utf-8') as file:

                for url in self.vulnerable_urls:

                    file.write(f"{url}\n")

            print(f"{Color.GREEN}Vulnerable URLs saved to {filename}{Color.RESET}")

        except Exception as e:

            print(f"{Color.RED}Error saving vulnerable URLs to file: {e}{Color.RESET}")



    def main(self):

        print(Color.RED + r"""

      ██████╗ ██╗     ██╗███╗   ██╗██████╗      ███████╗ ██████╗ ██╗
      ██╔══██╗██║     ██║████╗  ██║██╔══██╗     ██╔════╝██╔═══██╗██║
      ██████╔╝██║     ██║██╔██╗ ██║██║  ██║     ███████╗██║   ██║██║
      ██╔══██╗██║     ██║██║╚██╗██║██║  ██║     ╚════██║██║   ██║██║
      ██████╔╝███████╗██║██║ ╚████║██████╔╝     ███████║╚██████╔╝███████╗
      ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝╚═════╝      ╚══════╝ ╚═════╝ ╚══════╝



      Blind SQL Injection Scanner

      Created by HARZE12

      GitHub: https://github.com/HARZE12



        """ + Color.RESET)



        # Input for URL or URL list file

        input_url_or_file = input(Color.BLUE + "Enter the URL or path to the URL list file: " + Color.RESET).strip()

        if not input_url_or_file:

            print(f"{Color.RED}No URL or URL list file provided.{Color.RESET}")

            return



        urls = [input_url_or_file] if not os.path.isfile(input_url_or_file) else self.read_file(input_url_or_file)

        if not urls:

            print(f"{Color.RED}No valid URLs provided.{Color.RESET}")

            return



        # Input for payload file

        payload_path = input(Color.BLUE + "Enter the full path to the payload file (e.g., payloads/xor.txt): " + Color.RESET).strip()

        payloads = self.read_file(payload_path)

        if not payloads:

            print(f"{Color.RED}No valid payloads found in file: {payload_path}{Color.RESET}")

            return



        # Input for cookie

        cookie = input(Color.BLUE + "Enter the cookie to include in the GET request (leave empty if none): " + Color.RESET).strip()



        # Input for proxy

        proxy_input = input(Color.BLUE + "Enter proxy address (e.g., http://127.0.0.1:8080, leave empty for no proxy): " + Color.RESET).strip()

        if proxy_input:

            self.set_proxy(proxy_input)



        # Input for verbose mode

        verbose_input = input(Color.BLUE + "Enable verbose mode? (y/n): " + Color.RESET).strip().lower()

        if verbose_input in ['y', 'yes']:

            self.verbose = True



        # Input for thread count

        threads = input(Color.BLUE + "Enter the number of threads (0 for sequential execution): " + Color.RESET).strip()

        try:

            threads = int(threads)

        except ValueError:

            print(f"{Color.RED}Invalid input. Using sequential execution.{Color.RESET}")

            threads = 0



        print(f"\n{Color.BLUE}Starting scan...{Color.RESET}")



        try:

            if threads == 0:

                # Sequential mode (safe for time-based payloads)

                for url in urls:

                    for payload in payloads:

                        self.total_tests += 1

                        success, url_with_payload, response_time, status_code, error_message = self.perform_request(url, payload, cookie)

                        if success and status_code and response_time >= 10:  # Example threshold

                            self.vulnerabilities_found += 1

                            self.vulnerable_urls.append(url_with_payload)

                            if self.verbose:

                                print(f"{Color.GREEN}🟢 SQLi Found! URL: {url_with_payload} - Response Time: {response_time:.2f} seconds - Status Code: {status_code}{Color.RESET}")

                            else:

                                print(f"{Color.GREEN}🟢 Vulnerable URL: {url_with_payload}{Color.RESET}")

                        else:

                            if self.verbose:

                                print(f"{Color.RED}🔴 Not Vulnerable: {url_with_payload} - Response Time: {response_time:.2f} seconds - Status Code: {status_code}{Color.RESET}")



            else:

                # Concurrent mode (not recommended for time-based payloads)

                with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:

                    futures = [executor.submit(self.perform_request, url, payload, cookie) for url in urls for payload in payloads]

                    for future in concurrent.futures.as_completed(futures):

                        self.total_tests += 1

                        success, url_with_payload, response_time, status_code, error_message = future.result()

                        if success and status_code and response_time >= 10:  # Example threshold

                            self.vulnerabilities_found += 1

                            self.vulnerable_urls.append(url_with_payload)

                            if self.verbose:

                                print(f"{Color.GREEN}🟢 SQLi Found! URL: {url_with_payload} - Response Time: {response_time:.2f} seconds - Status Code: {status_code}{Color.RESET}")

                            else:

                                print(f"{Color.GREEN}🟢 Vulnerable URL: {url_with_payload}{Color.RESET}")

                        else:

                            if self.verbose:

                                print(f"{Color.RED}🔴 Not Vulnerable: {url_with_payload} - Response Time: {response_time:.2f} seconds - Status Code: {status_code}{Color.RESET}")



        except KeyboardInterrupt:

            print(f"{Color.YELLOW}Scan interrupted by user.{Color.RESET}")



        print(f"\n{Color.BLUE}Scan Complete.{Color.RESET}")

        print(f"{Color.YELLOW}Total Tests: {self.total_tests}{Color.RESET}")

        print(f"{Color.GREEN}Blind SQLi Found: {self.vulnerabilities_found}{Color.RESET}")

        if self.vulnerabilities_found > 0:

            print(f"{Color.GREEN}🟢 Your scan has found {self.vulnerabilities_found} vulnerabilities!{Color.RESET}")

        else:

            print(f"{Color.RED}🔴 No vulnerabilities found. Better luck next time!{Color.RESET}")



        # Save vulnerable URLs to file

        save_file = input(Color.BLUE + "Enter the filename to save results (leave empty to skip): " + Color.RESET).strip()

        if save_file:

            self.save_vulnerable_urls(save_file)



        print(f"{Color.BLUE}Thank you for using Blind SQL Scanner by HARZE12!{Color.RESET}")





if __name__ == "__main__":

    scanner = BSS()

    scanner.main()
