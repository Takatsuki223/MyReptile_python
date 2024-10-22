from bs4 import BeautifulSoup
import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
contents = requests.get("https://www.baidu.com/",headers = headers)

print(contents.status_code)
content = contents.text



soup = BeautifulSoup(content,"html.parser")
all_name = soup.findAll("span",attrs={"class":"title-content-title"})
for name in all_name:
    print(name.string)
    # sss = name.find("a")
    # print(sss)