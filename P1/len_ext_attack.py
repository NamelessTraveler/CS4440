import http.client as httplib
from urllib.parse import urlparse, quote
import sys, re
from pymd5 import md5, padding

url = sys.argv[1]
# Your code to modify the URL goes here!

appendText = "&command3=UnlockAllSafes"

index0 = url.find('=')
pre = url[0:index0+1]
print(pre)

index1 = url.find('&')
originalToken = url[index0+1:index1]
print(originalToken)

originalText = url[index1:url.__len__()]
print(originalText)

targeText = originalText+appendText
print(targeText)



parsedUrl = urlparse(url)
conn = httplib.HTTPConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print(conn.getresponse().read())



