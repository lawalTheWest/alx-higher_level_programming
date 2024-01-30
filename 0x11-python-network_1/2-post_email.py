#!/usr/bin/python3
'''
    this script takes in a URL and Email:
    sends a POST request toi the URL with the email as parameter.
    displays the body of the response (decoded in uTF-8)
'''

import urllib.request
from sys import argv
import urllib.parse


if __name__ == '__main__':
    my_url = argv[1]
    my_parameter = {'email': argv[2]}
    my_data = urllib.parse.urlencode(my_parameter)
    my_data = my_data.encode('ascii')
    my_request = urllib.request.Request(my_url, my_data)
    with urllib.request.urlopen(my_request) as response:
        print(response.read().decode())
