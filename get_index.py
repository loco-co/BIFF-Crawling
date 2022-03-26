import requests
from bs4 import BeautifulSoup

URL = f'http://www.biff.kr/kor/html/archive/arc_history_2.asp'

max_page = 20

def extract_pages():
    page = []
    for page_num in range(1, max_page+1):
        result = requests.get(f'{URL}?page={page_num}&pyear=2020&pn=&s1=&sn=&c1=&cn=')
        soup = BeautifulSoup(result.text, "html.parser")

        pg_li = soup.find_all('a', {"class": "film_thumb"})

        for pg in pg_li:
            index = (pg.get('href'))
            link = "http://www.biff.kr/kor/html/archive/" + index
            page.append(link)

    print(page)
    return page
