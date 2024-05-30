

import urllib.request

weburl = urllib.request.urlopen('http://www.weather.gov')
print("Result code: ", weburl.getcode())
data = weburl.read()
print(data)







