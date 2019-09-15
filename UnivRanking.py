#!/usr/bin/python3
import requests, bs4
url="http://www.zuihaodaxue.cn/BCSR/huaxue2017.html"
res=requests.get(url) 
res.encoding=res.apparent_encoding
soup=bs4.BeautifulSoup(res.text,'html.parser')
#print soup.tbody('tr')
s=''
for elem in soup.tbody('tr')[:-1]:
    for i in elem.descendants:
        if type(i) == bs4.element.NavigableString:
            s+=i+'\t'
        elif i.string == None:
            break
    s+='\n'
print(s)
