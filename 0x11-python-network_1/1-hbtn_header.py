#!/usr/bin/python3
'''
    This script takes in a URL and sends a request to the URL
    and displays the value of the variable found in the header of the response
'''
import urllib.request
from sys import argv

if __name__ == '__main__':
    my_request = urllib.request.Request(argv[1])
    with urllib.request.urlopen(my_request) as response:
        value = response.getheader('X-Request-Id')
        print(value)
