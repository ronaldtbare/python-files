

import urllib.request
import json

def printResults(data):
    theJSON = json.loads(data)

    print(theJSON)


urldata = "https://api.weather.gov/openapi.json"

weburl = urllib.request.urlopen(urldata)
print("result code: ", str(weburl.getcode()))

if (weburl.getcode() == 200):
    data = weburl.read()
else:
    print("Error:  Server is down and cannot print resuls.", weburlgetcode())

printResults(data)
