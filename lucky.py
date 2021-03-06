#!/usr/bin/python
# lucky.py - Opens several google search results.
import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('https://www.google.com.hk/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text,'lxml')

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://www.google.com.hk' + linkElems[i].get('href'))
