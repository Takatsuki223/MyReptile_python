from bs4 import BeautifulSoup #从bs4引入！
import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}
content = requests.get("http://books.toscrape.com/",headers = headers).text
soup  = BeautifulSoup(content,"html.parser") #用构造函数解析，传入content
#soup就是漂亮汤的对象
print(soup.p)#第一个p元素（段落）若里面还有，里面东西也会出
print("\n")
print(soup.img)#第一个图片
print("\n")

all_price = soup.findAll("p",attrs={"class":"price_color"})
#一个方法，能更具指定的标签找出所有符合要求的元素
#中间填的是，p标签，attrs是个字典，找价格颜色的class元素
#找p标签，其中class为价格颜色的
#attrs为可选的！只是用来筛选其中的东西

for price in all_price:  #在这里面迭代！
    print(price) #这时候输出的是含价格price的标签，还不够简洁
    print(price.string)#打印对象的string属性！返回标签包围的文字
    print(price.string[2:]) #索引值大于等于2的所有字符串
    print("\n")

print("\n")
print("\n")
#若要爬书名
all_titles = soup.findAll("h3")
#此处不用筛选了！所有不用attrs
for title in all_titles:  #此处再迭代
    link = title.find("a")#再筛选一次！ h3里面再找a标签，因为里面都是a标签所以不用findAll
    print(link.string)
print("\n")
