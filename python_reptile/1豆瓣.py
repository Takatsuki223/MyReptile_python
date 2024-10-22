from http.client import responses
import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}
response = requests.get("https://movie.douban.com/top250",headers = headers)  #传入可选值head
print(response.status_code)   #看状态码  418错误！ developer.mozilla.org/zh-CN/docs/Web/HTTP/Status/418看具体
print(response.text)
