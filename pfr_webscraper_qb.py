from bs4 import BeautifulSoup
import requests

url = 'https://www.pro-football-reference.com/years/2018/passing.htm'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

for row in tb.find_all('tr'):
    i = row.get_text()
    print(i)