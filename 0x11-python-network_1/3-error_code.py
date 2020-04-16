#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL,
and displays the body of the response.
If an error is returned, the error code should be
printed.
"""
import urllib.request
import urllib.error
import sys


if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
