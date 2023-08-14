from urllib.request import urlopen
import requests, json
import os
from datetime import datetime, timedelta



def next_birthdate(dob='1992-09-08', unit='hour'):
    base_url = 'https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth='
    url = f'{base_url}{dob}&unit={unit}'
    try:
        r = requests.get(url)
    except Exception as e:
        print(f"\nException: {e}")
        return False, e
    if r.status_code == '200':
        print(f'Status Code: {r.status_code}\nResponse: {r.text}')
        return True, r.text
    else:
        print(f'Status Code: {r.status_code}\nResponse: {r.text}')
        return False, r.text



