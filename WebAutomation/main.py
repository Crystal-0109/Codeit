import requests

rating_pages = []
# https://https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=0

for i in range(5):
    url = "https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex={}".format(i)
    response = requests.get(url)
    rating_page = response.text
    rating_pages.append(rating_page)
    
print(len(rating_pages))
print(rating_pages[0])
