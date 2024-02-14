import requests
from bs4 import BeautifulSoup


response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

program_title_tags = soup.select('td.program')

program_titles = []

for tag in program_title_tags:
    program_titles.append(tag.get_text())

print(program_titles)

# print(soup.select_one('td.program'))