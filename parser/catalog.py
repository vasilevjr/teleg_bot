import requests
from bs4 import BeautifulSoup



URL = "https://voda59.ru/catalog"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

def get_html(url):
    response = requests.get(url, headers=HEADERS)
    return response

def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="pc")
    parsed_data = []
    for item in items:
        parsed_data.append({
            "title": item.find('h3', class_='head head-sm head_c_dark_blue pc__head').getText(),
            "info": item.find('ul', class_='pc__ul').getText(),
            "price": item.find('div', class_='pc__price-new').getText(),
            "img": item.find('img').get('src')
        })
        return parsed_data


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        parsed_data = get_data(html.text)
        return parsed_data
    raise Exception("Ошибка в парсере!")



