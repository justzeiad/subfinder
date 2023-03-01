import argparse
import sys
import requests
import pyfiglet
from datetime import datetime
import threading
from concurrent.futures import ThreadPoolExecutor

def Header():
    print(pyfiglet.figlet_format("SUB FINDER"))
    print(pyfiglet.figlet_format("Made By Yuu", font="digital"))
    print("-" * 50)
    print("Scaning Start At: ", str(datetime.now()))
    print("-" * 50)


class SubFinder:
    def __init__(self, domain, output=None, threads=5, wordlist=None, verbose=False):
        self.domain = domain
        self.output = output
        self.threads = threads
        self.wordlist = wordlist
        self.verbose = verbose
        
    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description="Subdomain enumeration tool")
    
        parser.add_argument("domain", help="The domain to scan")
        parser.add_argument("-o", "--output", help="Output file name")
        parser.add_argument("-t", "--threads", type=int, default=5, help="Number of threads to use")
        parser.add_argument("-w", "--wordlist", help="Path to the wordlist file", required=True)
        parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
        
        return parser.parse_args()
        
    def scan_subdomain(self, subdomain):
        try:
            response = requests.get(f'https://{subdomain}')

        except requests.exceptions.RequestException:
            return None

        except KeyboardInterrupt:
            print("\n \033[1;33;40mExiting Program !\033[0m")
            sys.exit()

        if response.status_code < 400:
            print(f"\033[32m [+] \033[0m {subdomain}")
            return subdomain

        return None
        
    def enumerate_subdomains(self):
        subdomains = set()
        stop_event = threading.Event()
        try:
            with open(self.wordlist, 'r') as wordlist:
                with ThreadPoolExecutor(max_workers=self.threads) as executor:
                    futures = []
                    for line in wordlist:
                        subdomain = line.strip() + '.' + self.domain
                        futures.append(executor.submit(self.scan_subdomain, subdomain))

                    for future in futures:
                        subdomain = future.result()
                        if subdomain:
                            subdomains.add(subdomain)

        except KeyboardInterrupt:
            print("\n \033[1;33;40mExiting Program !\033[0m")
            stop_event.set()
            sys.exit()            

        if stop_event.is_set():
            return set()

        if self.output:
            with open(self.output, 'w') as f:
                f.write('\n'.join(subdomains))
                
        if self.verbose:
            print('\n'.join(subdomains))
        return subdomains


Header()

if __name__ == "__main__":
    args = SubFinder.get_args()
    subfinder = SubFinder(args.domain, output=args.output, threads=args.threads, wordlist=args.wordlist, verbose=args.verbose)
    subdomains = subfinder.enumerate_subdomains()
