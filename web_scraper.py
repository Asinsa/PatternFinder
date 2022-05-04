import requests
from bs4 import BeautifulSoup
import os
from os.path import exists


# Scrape and parse HTML content from page
def soupify(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


# Gets all the sections from the year provided
def get_section(yearURL):
    dataset = soupify(baseURL + yearURL).find('ul', {'class': 'mb-0 block-list'})

    for data in dataset:
        newsoup = BeautifulSoup(str(data), 'html.parser')
        links = newsoup.findAll('a', {'class': 'list-title td-none td-ul-hover'})
        for link in links:
            link = link.get("href").strip("..")
            year = link[-4:]
            section = link[link.find("Component=") + len("Component="):link.find("&")]
            if section != 'LimitedAccess':
                get_download_link(link, year, section)
                print("FINISHED DOWNLOADING " + section + "\n")


# Gets the download link for the each file in the corresponding year and section
def get_download_link(sectionURL, year, section):
    dataset = soupify(baseURL + sectionURL).find('tbody')

    for data in dataset:
        newsoup = BeautifulSoup(str(data), 'html.parser')
        links = newsoup.findAll('a')
        for link in links:
            dataFileLink = link.get("href")
            if dataFileLink.endswith('.XPT'):
                download('https://wwwn.cdc.gov/' + dataFileLink, dest_folder="NHANES/" + year + "/" + section)


# Saves the file locally to a folder called NHANES
def download(url: str, dest_folder: str):
    if not exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist

    filename = url.split('/')[-1].replace(" ", "_")
    file_path = os.path.join(dest_folder, filename)

    if not exists(file_path):
        r = requests.get(url, stream=True)
        if r.ok:
            print("Saving to", os.path.abspath(file_path))
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 8):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        os.fsync(f.fileno())
        else:  # HTTP status code 4XX/5XX
            print("Download failed: status code {}\n{}".format(r.status_code, r.text))


baseURL = "https://wwwn.cdc.gov/nchs/nhanes"

# Forms the correct base URL for each year
for year in range(1999, 2015)[::-1]:
    if year % 2 != 0:
        get_section('/continuousnhanes/default.aspx?BeginYear=' + str(year))
        print("--FINISHED DOWNLOADING " + str(year) + "--\n\n")

