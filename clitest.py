#!/home/ec2-user/DjangoDRFenv/env/bin/python
"""
Command line sanity checking of Django DRF project
This is not a production set of tests, rather it is a simple mechanism that
allowed me to understand the DRF using tools I was more familiar with
(I also did command line `curl` testing)

This script performs:
 - Get /      -- to list all items
 - POST       -- to add a new item
 - GET /id    -- to get details of one items
 - DELETE / id   -- delete an item
 - Get /         -- 2nd list to confirm previous add/delete
"""

import requests
headers = {'Content-Type' : 'application/json'}

baseurl = 'http://127.0.0.1/api/v1/wishlist'


### Generate a query to list all wishlist items
url = baseurl
print('GET /')
response = requests.get(url,headers=headers, timeout = 2)
print(response.url)
jout = response.text.replace('},','},\n')
print(response.status_code)
print(jout)
print('--------------')

### Generate a query to create a new wishlist book item
url = 'http://127.0.0.1/api/v1/wishlist/'
print('POST /id')
params = { 'name' : 'JJJ', 'bid' : '3333' }
response = requests.post(url,headers=headers,json=params)
print(response.url)
print(response.status_code)
print(response.text)
print('--------------')

### Generate a query to get details of a single wishlist item
print('GET /id')
url = baseurl + '/1'
response = requests.get(url,headers=headers)
print(response.url)
print(response.status_code)
print(response.text)
print('--------------')


### Generate a query to delete a wishlish item
print('DELETE /id')
url = baseurl + '/25'
response = requests.delete(url,headers=headers)
print(response.url)
print(response.status_code)
print(response.text)
print('--------------')


### Generate a 2nd query to list all wishlist items
### (to confirm effects of previous insert/delete)
url = baseurl
print('GET /')
response = requests.get(url,headers=headers, timeout = 2)
print(response.url)
jout = response.text.replace('},','},\n')
print(response.status_code)
print(jout)
print('--------------')

