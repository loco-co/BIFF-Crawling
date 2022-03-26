from get_index import extract_pages
from get_data import get_data
from save import save_to_csv

# pages = extract_pages()

# print(pages)

movie_data = get_data()

# print(movie_data)

save_to_csv(movie_data)
