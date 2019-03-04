import urllib.request, urllib.parse, urllib.error
import re

url = input('Enter URL: ')

try:
    html = urllib.request.urlopen(url).read()
except:
    print("The URL can not be opened!")
else:
    st = html.lower()

    links1 = re.findall(b'href="(https?://.*?)"', st)

    counts = dict()
    for line in links1:
        words = line.decode().split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
    print("The number of unique web links on your page is:",len(counts))
