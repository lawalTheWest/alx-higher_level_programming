#!/usr/bin/python3
'''
    This script fetches a given URL
'''
import requests


if __name__ == '__main__':
    my_url = 'http://alx-intranet.hbtn.io/status'
    my_request = requests.get(my_url)
    print('Body response:')
    print('\t- type: {}'.format(type(my_request.text)))
    print('\t- content: {}'.format(my_request.text))
