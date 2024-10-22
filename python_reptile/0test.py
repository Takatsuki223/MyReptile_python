import requests
head = { "User-Agent":"Mozilla/5.0 (Windows NT 10.0; win64; x64)"}
#用于伪装成浏览器的键值对，写明用户代理
response = requests.get("http://books.toscrape.com")
print(response)#输出这个response实例   200成功
if response.ok:         #若请求成功
    print(response.status_code)
    #print(response.text)  #该方法将网站以html的形式爬
else:
    print("失败！")

from http.client import responses
import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}
response = requests.get("https://www.bilibili.com/video/BV12x4TepEw1/?share_source=copy_web&vd_source=7cad1ff274ed85c0633e186a8156cc65",headers = headers)  #传入可选值head
print(response.status_code)   #看状态码  418错误！ developer.mozilla.org/zh-CN/docs/Web/HTTP/Status/418看具体
print(response.text)
