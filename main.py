import requests
from bs4 import BeautifulSoup

URL = "https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?BeginYear=2017"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

dataset = soup.find('ul', {'class': 'mb-0 block-list'})

for data in dataset:
    newsoup = BeautifulSoup(str(data), 'html.parser')
    links = newsoup.findAll('a', {'class': 'list-title td-none td-ul-hover'})
    for link in links:
        print(link.get("href"))

