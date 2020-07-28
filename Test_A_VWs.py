import requests
from bs4 import BeautifulSoup
import pandas as pd

# 请求URL

url = 'http://car.bitauto.com/xuanchegongju/?l=8&mid=8'
# 得到页面的内容
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
html=requests.get(url,headers=headers,timeout=10)
content = html.text

# 通过content创建BeautifulSoup对象
soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')

temp = soup.find('div',class_="search-result-list")

list_all = temp.find_all('div',class_="search-result-list-item")
for list in list_all:
    img = list.find('img',class_="img")
    name = list.find(class_= "cx-name text-hover")
    price =list.find (class_="cx-price")
    print ('\n',img,'\n',name.text,'\n',price.text,'\n')
