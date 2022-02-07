from bs4 import BeautifulSoup
import pandas as pd
import requests

text = []
date = []

html_text = requests.get('http://kenesh.kg/ru').text
soup = BeautifulSoup(html_text, 'lxml')

news = soup.find_all('div', class_ = 'news-item-row-info')
for new in news:
    date.append(new.find('span').text.replace(' ', '').replace('\n', ''))
    text.append(new.find('h3', class_="news-item-row-title").text)

df = pd.DataFrame(list(zip(text,date)),
               columns =['Title', 'Date'])

t1 = text[0]
t2 = text[1]
t3 = text[2]

d1 = date[0]
d2 = date[1]
d3 = date[2]