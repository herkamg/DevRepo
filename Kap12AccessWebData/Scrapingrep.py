import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
url = input('Enter URL - ')
#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
count = int(input('counts - '))
position = int(input('position - '))
counts = 0
while counts < count:
    #url = input('Enter URL - ')
    #url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
    html = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(html, 'html.parser')
    i = 0
    # Retrieve all tag <span>
    tags = soup('a')
    #print(tags)
    for tag in tags:
    #    print(tag)
        if i == position-1:
            url = tag.get('href', None)
            print(url)
        i = i + 1

    counts = counts + 1
