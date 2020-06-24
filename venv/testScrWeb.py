import requests
from bs4 import BeautifulSoup

res = requests.get('https://newhouse.fang.com/house/s/')
soup = BeautifulSoup(res.text,'html.parser')
# print(soup.prettify())
print(soup.select('#sjina_C21_02 > a'))





