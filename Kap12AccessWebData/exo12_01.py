import urllib.parse, urllib.request, urllib.error
import xml.etree.ElementTree as ET
import ssl


counts = 0
# enforce HTTPS: ignore ssl certifaces errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
searchUrl = input('Enter Url: ')
#searchUrl = 'http://py4e-data.dr-chuck.net/comments_42.xml'
# open the url and read the data
data = urllib.request.urlopen(searchUrl, context = ctx).read()
#data = urllib.request.urlopen(searchUrl).read()

Tree = ET.fromstring(data)


listOfComments = Tree.findall('comments/comment')
#print('number of comments: ', len(listOfComments))

for comment in listOfComments:
    # print('name :', comment.find('name').text)
    # print('count:', comment.find('count').text)
    counts = counts + int(comment.find('count').text)
print('summe of counts: ' , counts)
