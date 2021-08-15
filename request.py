'''
get and post request template

proxy through BURP
or
Certificates
'''

import request
import urllib
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib.disable_warnings(InsecureRequestWarning)

proxy = {
    'https': 'http://127.0.0.1:8080',
    'http': 'http://127.0.0.1:8080'
}

#cert = ('/home/fafnir/cert/6843.pem', '/home/fafnir/cert/6843.key')

'''
GET requests 
'''

url = ""
request.get(url, proxies=proxy, verify=False)


'''
POST requests
'''
