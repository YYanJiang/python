import urllib.request, urllib.parse, urllib.error
import re


url = input('Enter URL: ')

html = urllib.request.urlopen(url).read()

links1 = re.findall(b'href="(http://.*?)"', html)
links2 = re.findall(b'href="(HTTP://.*?)"', html)

counts = dict()
num = 0
for line in html:
    lin = line.decode()
    num = num + 1
print(num)