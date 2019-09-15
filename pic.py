#!/usr/bin/python3
import requests
import bs4
import os
url="https://www.google.com.hk/search?tbm=isch"
pic=input("你想下载什么图片?\n")+'/'
q={'q': pic}
os.makedirs(pic, exist_ok=True)
res=requests.get(url,params=q)
print(res.status_code)
res.encoding=res.apparent_encoding
#print(res.text)
soup=bs4.BeautifulSoup(res.text,'html.parser')
img=soup('img')
n=0
for i in img:
    n+=1
    link=i.get('src')
    #print(link)
    r=requests.get(link)
    print("正在下载第",n,"张图片")
    with open(pic+os.path.basename(link).split(':')[1]+'.jpg','wb') as f:
        f.write(r.content)
    print("第",n,"张图片下载完成")
