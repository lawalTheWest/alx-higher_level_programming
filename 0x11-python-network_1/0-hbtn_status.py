#!/usr/bin/python3
'''
    The python script that fetches "https://alx-intranet.hbtn.io/status"

    Usage: ./0-hbtn_status.py | cat -e
'''
import urllib.request
with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    html = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
    print('\t- utf8 content: {}'.format(html.decode('utf-8')))

