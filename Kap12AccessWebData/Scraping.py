import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = input('Enter URL - ')
#url = 'http://py4e-data.dr-chuck.net/comments_702221.html'
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')
summe = 0
# Retrieve all tag <span>
tags = soup('span')
for tag in tags:
    #print(tag)
    line = str(tag)
    #print(line)
    comments= re.findall("[0-9]+",line)
    summe = summe + int(comments[0])
    #print(comments)
print(summe)
