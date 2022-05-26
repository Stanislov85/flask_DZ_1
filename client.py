import requests

HOST = 'http://127.0.0.1:5000/hello/'
data = requests.get(HOST)
print(data.text)