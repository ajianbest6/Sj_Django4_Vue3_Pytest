import requests


resp = requests.request(method="get", url="https://www.baidu.com")

print(resp.status_code)
print(resp.headers)
print(resp.text)
