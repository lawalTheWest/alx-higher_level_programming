#!/usr/bin/python3
'''
    given URL & email as parameters,
    sends POST request to URL,
    displays response body utf-8
    usage: ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
'''
import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    pyld = {'email': argv[2]}
    rqst = requests.post(url, data=pyld)
    print(rqst.text)
