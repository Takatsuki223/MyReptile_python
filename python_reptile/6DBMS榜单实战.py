from bs4 import BeautifulSoup
import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}
content = requests.get("https://db-engines.com/en/ranking/relational+dbms",headers = headers)

print(content.status_code)
contents = content.text

soup = BeautifulSoup(contents,"html.parser")

all_th = soup.findAll("th",attrs={"class":"pad-l"})
for th in all_th:
    a = th.find("a")
    a_text = a.text
    #if "Detailed" not in a_text:  #!!重要操作。若字段不在才输出整段

    gun = "Detailed vendor-provided information available" #定义要去除的字段
    if "Detailed" in a_text:       #判断在不在这，若在去除
        a = a_text[:-len(gun)].strip()  #减去要去除字段的长度！  平时的用法[3:]:左数3个字符不输出、[:3]：仅保留左数3个字符
        print(a)
    else:
        print(a_text)                   #输出DBMS榜上的名字，同网站排序




