import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find('div', id='catalog_title_block').find('h1', itemprop='name').text
    return h1


def main():
    url = 'https://rozetka.com.ua/ua/notebooks/c80004/filter/producer=hp-hewlett-packard;sort=cheap;20861=6305/'
    print(get_data((get_html(url))))



if __name__ == '__main__':
    main()
