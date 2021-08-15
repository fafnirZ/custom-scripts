'''
get and post request template

proxy through BURP
or
Certificates
'''

import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

proxy = {
    'https': 'http://127.0.0.1:8080',
    'http': 'http://127.0.0.1:8080'
}

#cert = ('/home/fafnir/cert/6843.pem', '/home/fafnir/cert/6843.key')

'''
GET requests
'''

url = ""
response = requests.get(url, proxies=proxy, verify=False)
print(response.text)


'''
POST requests
'''