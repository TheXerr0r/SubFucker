#!/usr/bin/python3

import argparse
import requests
import os
import time
import sys
import colorama
from concurrent.futures import ThreadPoolExecutor
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.exceptions import *
from tabulate import tabulate
from colorama import Fore, Style

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class colors:
    yellow = Fore.LIGHTYELLOW_EX
    black = Fore.LIGHTBLACK_EX
    blue = Fore.LIGHTBLUE_EX
    magenta = Fore.LIGHTMAGENTA_EX
    red = Fore.LIGHTRED_EX
    cyan = Fore.LIGHTCYAN_EX
    green = Fore.LIGHTGREEN_EX
    white = Fore.LIGHTWHITE_EX
col = colors()


class SubFucker:
    def __init__(self, inputfile, outfile, tn):
        self.tn = tn
        self.inputfile = inputfile
        self.outfile = outfile
        self.status_success = [""]
        self.all_status = [""]
        with open(self.inputfile) as file:
            self.subs_file = [line.strip("\n") for line in file]
    
    def save(self):  
        with open(self.outfile, 'a') as f:
            content = self.status_success
            for lines in content:
                if lines:
                    f.write(f"{lines.strip()}\n")
        with open("All_subs.txt", 'a') as allSubs:
            content = self.status_success + self.all_status
            for lin3 in content:
                if lin3:
                    allSubs.write(f"{lin3.strip()}\n")

    def parce(self, url):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Content-Type': 'application/json',
        }
        status_dict = {
                    # 1xx Informational - HTTP Status Codes
        100 : "Continue",
        101 : "Switching Protocols",
        102 : "Processing (WebDAV)",
        103 : "Early Hints",
                    # 2xx Success - HTTP Status Codes
        201 : "Created",
        202 : "Accepted",
        203 : "Non-Authoritative Information",
        204 : "No Content",
        205 : "Reset Content",
        206 : "Partial Content",
        207 : "Multi-Status (WebDAV)",
        208 : "Already Reported (WebDAV)",
        226 : "IM Used",
                    # 3xx Redirection - HTTP Status Codes
        300 : "Multiple Choices",
        301 : "Moved Permanently",
        302 : "Found",
        303 : "See Other",
        304 : "Not Modified",
        305 : "Use Proxy",
        306 : "(Unused)",
        307 : "Temporary Redirect",
        308 : "Permanent Redirect (experimental)",
                    # 4xx Client Error - HTTP Status Codes
        400 : "Bad Request",
        401 : "Unauthorized",
        402 : "Payment Required",
        403 : "Forbidden",
        404 : "Not Found",
        405 : "Method Not Allowed",
        406 : "Not Acceptable",
        407 : "Proxy Authentication Required",
        408 : "Request Timeout",
        409 : "Conflict",
        410 : "Gone",
        411 : "Length Required",
        412 : "Precondition Failed",
        413 : "Request Entity Too Large",
        414 : "Request-URI Too Long",
        415 : "Unsupported Media Type",
        416 : "Requested Range Not Satisfiable",
        417 : "Expectation Failed",
        418 : "I'm a teapot (RFC 2324)",
        420 : "Enhance Your Calm (Twitter)",
        421 : "Misdirected Request",
        422 : "Unprocessable Entity (WebDAV)",
        423 : "Locked (WebDAV)",
        424 : "Failed Dependency (WebDAV)",
        425 : "Reserved for WebDAV",
        426 : "Upgrade Required",
        428 : "Precondition Required",
        429 : "Too Many Requests",
        431 : "Request Header Fields Too Large",
        444 : "No Response (Nginx)",
        449 : "Retry With (Microsoft)",
        450 : "Blocked by Windows Parental Controls (Microsoft)",
        451 : "Unavailable For Legal Reasons",
        499 : "Client Closed Request (Nginx)",
                    # 5xx Server Error - HTTP Status Codes
        500 : "Internal Server Error",
        501 : "Not Implemented",
        502 : "Bad Gateway",
        503 : "Service Unavailable",
        504 : "Gateway Timeout",
        505 : "HTTP Version Not Supported",
        506 : "Variant Also Negotiates (Experimental)",
        507 : "Insufficient Storage (WebDAV)",
        508 : "Loop Detected (WebDAV)",
        509 : "Bandwidth Limit Exceeded (Apache)",
        510 : "Not Extended",
        511 : "Network Authentication Required",
        598 : "Network read timeout error",
        599 : "Network connect timeout error",
    }
        try:
            subd_http = f"http://{url}/"  
            subd_https = f"https://{url}/"
            r = requests.get(subd_http, headers=headers, verify=False, timeout=5, allow_redirects=False)
            r2 = requests.get(subd_https, headers=headers, verify=False, timeout=5, allow_redirects=False)
            if len(r.content) > len(r2.content):
                if r.url == subd_http:
                    print(col.cyan + "\n\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-Request With Both HTTP Protocols-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                    if r.status_code == 200:
                        print("\n" + col.cyan + tabulate([[url, subd_http, r.status_code]], headers=['Domain', 'Response With HTTP', 'Status Code']))
                        self.status_success.append(r.url)
                    elif r.status_code in status_dict.keys():
                        print("\n" + col.red + tabulate([[subd_http,f"<HTTP Status Code {r.status_code}>", f"{status_dict[r.status_code]}"]], headers=['Domain', 'Response With HTTP', 'Status Code']) + Style.RESET_ALL)
            else:
                if r2.url == subd_https:
                    if r2.status_code == 200:
                        print("\n" + col.cyan + tabulate([[url, subd_https, r2.status_code]], headers=['Domain', 'Response With HTTPS', 'Status Code']) + Style.RESET_ALL)
                        self.status_success.append(r2.url)
                    elif r2.status_code in status_dict.keys():
                        print("\n" + col.red + tabulate([[subd_https,f"<HTTP Status Code {r2.status_code}>", f"{status_dict[r2.status_code]}"]], headers=['Domain', 'Response With HTTPS', 'Status Code']) + Style.RESET_ALL)
            self.all_status.append(r.url)
        except (ConnectionError, RequestException):
            pass


    @staticmethod
    def banner():
        print(col.cyan + """
        _________________________
       ( SubFucker Is Running Now )
          [!] Do Not Press CTL+C
        -------------------------
            o   ^__^                    | Created By TheXerr0r & MrJico
             o  (oo)\_______            | Scorpion Shiled Hackers Team - <Scorpion-Shield.Com>
                (__)\       )\/\        | Security is Our Game...
                    ||----w |
                    ||     ||  {v1.0.1}
        """ + Style.RESET_ALL)

    @staticmethod
    def CLS():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("reset")

    def run(self):
        self.CLS()
        self.banner()
        try:
            with ThreadPoolExecutor(max_workers=self.tn) as thread:
                thread.map(self.parce, self.subs_file)
        
        finally:
            self.save()
            print(col.cyan + "\n\n\t\t\tThis Fucken Proccess Is Completed Successfully :)\n")
            print(tabulate([[]], headers=['Life URLs Is Saved In ']))
            print(os.getcwd())
            Style.RESET_ALL
            exit()


def main():
    try:
        parser = argparse.ArgumentParser(description='Subfucker is a tool for enumerating subdomain status codes')
        parser.add_argument('-f' , '--inputfile', help='input file with subdomain, seperated by newline', required=True)
        parser.add_argument('-o' , '--outfile', help='output file name', required=True)
        parser.add_argument('-t' , '--threads', help='number of threads to use , default is 10', required=False, default=10, type=int)
        args = parser.parse_args()
        input_file = args.inputfile
        out_file = args.outfile
        nthread = args.threads
        runer = SubFucker(input_file, out_file, nthread)
        runer.run()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
