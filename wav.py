#!/usr/bin/python3
import requests
import bs4
import os
url="http://www.grsites.com/archive/sounds/category/23/"
os.makedirs('wav', exist_ok=True)
res=requests.get(url)
print(res.status_code)
res.encoding=res.apparent_encoding
#print(res.text)
soup=bs4.BeautifulSoup(res.text,'html.parser')
wav=soup.find_all('a',text='WAV')
print("一共有" + str(len(wav)) + "首歌曲")
n=0
for i in wav:
    n+=1
    #print(i)
    link=i.get('href')
    #print(link)
    r=requests.get(link)
    print("正在下载第",n,"首歌曲")
    with open('wav/'+os.path.basename(link),'wb') as f:
        f.write(r.content)
    print("第",n,"首歌曲下载完成")
