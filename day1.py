import requests
url="http://politics.people.com.cn/n1/2018/1020/c1001-30352747.html"
try:
    r=requests.get(url,timeout=5)
except requests.Timeout:
    print("程序超时")
if r.status_code==200:
    r.encoding=r.apparent_encoding
    print(r.text[-1000:])