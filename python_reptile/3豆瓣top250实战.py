from bs4 import BeautifulSoup
import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}

for start_num in range(0, 250 ,25): #其实是从0开始的，若再下一页是251，所以250正确 步长25
    #content = requests.get("https://movie.douban.com/top250",headers = headers).text 这还是只读一面的
    content = requests.get(f"https://movie.douban.com/top250?start={start_num}",headers = headers).text
    #使用Ff字符串方便填充！
    soup = BeautifulSoup(content,"html.parser") #指定html的解析器

    all_title1 = soup.findAll("span",attrs={"class":"title"}) #锁定class值为title的所有span

    for title1 in all_title1:
        #print(title.string)  #这时已经锁定了电影的名字，输出中文名和外文原名都会出来，有点麻烦！
        #所有原版标题前都有斜杠！以下是搞斜杠之前的方法
        title_string1 = title1.string
        if "/" not in title_string1:  #若不包含斜杠，才输出
            print(title_string1)
    #print("\n以上是直接锁定所有含有title的class的span标签的方法\n以下是先锁定div中hd的class，再逐个锁定a中第一个span的方法\n")

    # all_title2 = soup.findAll("div",attrs={"class":"hd"})  第二种全部输出的方式，先锁定class有hd的div，再锁定第一个a，再锁定第一个span
    # for title2 in all_title2:
    #     title3 = title2.find("a")
    #     print((title3.find("span")).string)