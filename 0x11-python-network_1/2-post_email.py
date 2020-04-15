#!/usr/bin/python3
"""python script that takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded utf-8)
"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    email = argv[2]

    data = {"email": email}
    values = urllib.parse.urlencode(data)
    values = values.encode("ascii")  # data should be bytes
    req = urllib.request.Request(url, values)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode("utf-8"))
