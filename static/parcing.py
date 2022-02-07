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
df
