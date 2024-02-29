from bs4 import BeautifulSoup
import requests

# CONSTANTS:
LIMIT_OF_MAXIMUM_ARTICLES_TO_DATA_SCRAPE = 100
print(f"Generating {LIMIT_OF_MAXIMUM_ARTICLES_TO_DATA_SCRAPE} Movies in the List... \n")

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')

# initialize an empty list to store article information
movies_list = []

title1 = ""


# Format for the Movie Title:   <h3 class="listicleItem_listicle-item__title__BfenH">100) Reservoir Dogs</h3>

# finds the article rows by their unique class 'athing'
article_rows = soup.find_all('h3', class_='listicleItem_listicle-item__title__BfenH', limit=LIMIT_OF_MAXIMUM_ARTICLES_TO_DATA_SCRAPE)

for row in article_rows:
    movies_list.append(row.text)


print(movies_list)
# print(movies_list.sort(reverse=False))
# articles_info.sort(key=lambda, reverse=True)

# # creates .txt file to write the full numbered list to:
# with open("100_Top_Movies-1.txt", mode="w") as file:
#     contents = file.write(f"The #1 Top article on this page with the most Upvotes (up to your Max limit) is:\n"
#                           f"Title of Article: {title1}\n"
#                           f"Article Link: {url1}\n"
#                           f"Upvotes Total: {upvotes1}\n")
