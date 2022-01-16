import requests
from bs4 import BeautifulSoup


def soupify(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def get_section(yearURL):
    dataset = soupify(baseURL + yearURL).find('ul', {'class': 'mb-0 block-list'})

    for data in dataset:
        newsoup = BeautifulSoup(str(data), 'html.parser')
        links = newsoup.findAll('a', {'class': 'list-title td-none td-ul-hover'})
        for link in links:
            download(baseURL + link.get("href").strip(".."))


def download(sectionURL):
    print(sectionURL)


baseURL = "https://wwwn.cdc.gov/nchs/nhanes"

for year in range(1999, 2019)[::-1]:
    if year % 2 != 0:
        get_section('/continuousnhanes/default.aspx?BeginYear=' + str(year))