import http.client as httplib
from urllib.parse import urlparse, quote
import sys, re
from pymd5 import md5, padding

url = sys.argv[1]
# Your code to modify the URL goes here!

appendText = "&command3=UnlockAllSafes"
originalurl = "http://cs4440.eng.utah.edu/project1/api?token=402a574d265dc212ee64970f159575d0&user=admin&command1=ListFiles&command2=NoOp"
pre = "http://cs4440.eng.utah.edu/project1/api?token="
originalText = "&user=admin&command1=ListFiles&command2=NoOp"
originalToken = "402a574d265dc212ee64970f159575d0"
targeText = originalText+appendText
print(pre)
print(originalToken)
print(targeText)
# parsedUrl = urlparse(url)
# conn = httplib.HTTPConnection(parsedUrl.hostname,parsedUrl.port)
# conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
# print(conn.getresponse().read())



