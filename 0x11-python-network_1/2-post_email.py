#!/usr/bin/python3
'''
    takes in a URL & email as a parameter,
    sends POST requests to the URL,
    Then ddisplays response body using the utf-8
    usage:./2-post_email.py
    http://0.0.0.0:5000/post_email hr@holbertonschool.com
'''
import urllib.request
from sys import argv
import urllib.parse


if __name__ == '__main__':
    received_url = argv[1]
    variable_sent = {'email': argv[2]}
    data = urllib.parse.urlencode(variable_sent)
    data = data.encode('ascii')
    requests_post = urllib.request.Request(received_url, data)

    with urllib.request.urlopen(requests_post) as response:
        print(response.read().decode())
