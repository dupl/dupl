#!/usr/bin/python
import requests
r=requests.get("https://item.jd.com/4585615.html")
print r.status_code
#r.encoding='utf-8'
print r.text[:1000]
