#!/usr/bin/python
import requests
import bs4
url='http://www.ip138.com/ips138.asp'
ip={'ip':raw_input("ip:")}
res=requests.get(url,params=ip)
res.encoding=res.apparent_encoding
soup=bs4.BeautifulSoup(res.text,'html.parser')
print soup.prettify()
elem=soup.select('li')
for i in elem:
    print i.getText()
