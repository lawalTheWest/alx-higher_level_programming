#!/usr/bin/python3
'''
    takes in the url,
    sends a request to the url and
    displays the body of the response decoded in utf-8
'''
import urllib.parse
import urllib.request
from sys import argv


if __name__ == '__main__':
    ''' try / exception '''
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode())
    except urllib.error.URLError as e:
        print('Error code: {}'.format(e.code))
