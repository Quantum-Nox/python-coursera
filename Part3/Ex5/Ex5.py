import json
import urllib.request, urllib.parse, urllib.error

#url = 'http://py4e-data.dr-chuck.net/comments_42.json'
url = 'http://py4e-data.dr-chuck.net/comments_24166.json'


uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

#    if not js or 'status' not in js or js['status'] != 'OK':
#    print('==== Failure To Retrieve ====')
#    print(data)

total = 0
for item in js['comments']:
    total = total + int(item["count"])

print(total)
