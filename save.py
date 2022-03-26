import csv

def save_to_csv(films):
    file = open("films.csv", mode="w", encoding="utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow\
        (["section", "title", "title_en", "detail", "synopsis", "director", "credit", "img_urls", "dir_img"])
    for film in films:
        writer.writerow(film)
    return
