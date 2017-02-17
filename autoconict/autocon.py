#!/usr/bin/env python
# coding=utf-8
import urllib
import urllib.parse
import urllib.request
import re

url = 'http://159.226.39.22/cgi-bin/do_login'
values = {'uname': '', 'pass': ''}
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows 10)'
headers = {'User-Agent': user_agent}
data = urllib.parse.urlencode(values)
data = data.decode("aciss")
request = urllib.request.Request(url, data)
response = urllib.request.urlopen(request)
con = response.read()
p = '\d*\D'
t = re.match(p, con)
if t == None:
    print("success")
pass
