import requests
from bs4 import BeautifulSoup
from get_index import extract_pages

def get_data():
    movie_data_all = []
    pages = extract_pages()
    # link = 'http://www.biff.kr/kor/html/archive/arc_history_2_view.asp?pyear=2020&s1=&page=12&m_idx=49603'
    for link in pages:
        movie = requests.get(link)
        soup = BeautifulSoup(movie.text, "html.parser")

        movie_data = []

        # 제목 구하기
        title_data = soup.find("div", {"class": "tit_wrap"})
        section = title_data.find("span").string
        title = title_data.find("h1").string
        title_en = title_data.find("p").string
        movie_data.append(section)
        movie_data.append(title)
        movie_data.append(title_en)

        # 정보 구하기
        film_data = soup.find("div", {"class": "pgv_film_info"})
        lis = film_data.find_all("li")
        film_info = []
        for li in lis:
            film_info.append(li.string)
        # print(film_info)
        movie_data.append(film_info)

        # 시놉시스
        pgnote = soup.find("div", {"class": "pgnote"})
        synopsis = pgnote.find("p").string
        if synopsis is not None:
            synopsis = synopsis.strip()
        # print(synopsis)
        movie_data.append(synopsis)

        # 감독 정보
        pgv_dir_info = soup.find("div", {"class": "pgv_dir_info"})
        dir_info = pgv_dir_info.find("p", {"class": "dir_desc desc mt10"}).string
        if dir_info is not None:
            dir_info = dir_info.strip()
        # print(dir_info)
        movie_data.append(dir_info)

        # 제작진 구하기
        credit_data = soup.find("ul", {"class": "credit_list"})
        lis = credit_data.find_all("li")
        credit = []
        for li in lis:
            credit.append(li.find("span").string)
        # print(credit)
        movie_data.append(credit)

        # 이미지 구하기
        movie_img = []
        thumbsimg = soup.find_all("div", {"class": "thumbsimg"})
        for img_meta in thumbsimg:
            img = 'http://www.biff' + img_meta.find("img")['src']
            movie_img.append(img)
        dir_img_thumb = soup.find("div", {"class": "thumb thumb-rounded"})
        dir_img = 'http://www.biff' + dir_img_thumb.find("img")['src']
        # print(movie_img)
        # print(dir_img)
        movie_data.append(movie_img)
        movie_data.append(dir_img)

        movie_data_all.append(movie_data)
        # print(movie_data)

    return movie_data_all
