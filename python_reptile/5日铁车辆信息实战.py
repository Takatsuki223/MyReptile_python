from cgi import print_form
from operator import length_hint

from bs4 import BeautifulSoup
import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}
content = requests.get("https://4gousya.net/",headers = headers)

print(f"status code:{content.status_code}")
contents = content.text

info = []
cars = []


soup = BeautifulSoup(contents,"html.parser")

# all_replace = soup.findAll("h2",attrs={"class":"entry-card-title card-title e-card-title"})
# print("\n編成表更新情報:")
# for c in all_replace:
#     print(c.string)

all_dayinfos = soup.find("div",attrs={"class":"col-sm-4"})  #只找当天的编成变化信息，因此仅需find
print("\n今日のフォーラム・グループの新着情報:")

all_titles = all_dayinfos.findAll("span",attrs={"class":"entry-title news-headline"})
for infos in all_titles:
    #print(infos.text )  #比.string更好用！直接输出有标签夹着的文本
    info.append(infos.text.strip())    #迭代的东西直接加入列表

all_cars = all_dayinfos.findAll("span",attrs={"class":"news-meta"})
for car in all_cars:
    cars.append(car.text[14:].strip()) #迭代的东西直接加入列表 .strip()去除空格，去掉了空换行

length = len(info)                     #反正东西个数一样，取一个列表的个数即可
i = 0
while i < length:
    print(info[i] +" - "+ cars[i])     #直接列表字符串拼接
    i+=1





