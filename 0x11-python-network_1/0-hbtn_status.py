#!/usr/bin/python3
import urllib.request
"""a Python script that fetches https://intranet.hbtn.io/status"""
if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as hbtn:
        status = hbtn.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(status), status, status.decode('utf-8')))
