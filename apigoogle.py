import requests
import json

#pip install requests
#pip intall json

token = 'Bearer <TOKEN>'
headers = {'Autoritation': token}
r = requests.get('https://google.com/', headers = headers)
r.status_code
print(r.status_code)