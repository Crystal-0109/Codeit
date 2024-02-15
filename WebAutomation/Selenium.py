from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet('플레이리스트')
ws.append(['제목', '해시태그', '좋아요 수', '곡 수'])

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/music')
time.sleep(1)

# 현재 scrollHeight 가져오기
last_height = driver.execute_script("return document.body.scrollHeight;")

while True:
    # scrollHeight까지 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 새로운 내용 로딩될때까지 기다림
    time.sleep(0.5)

    # 새로운 내용 로딩됐는지 확인
    new_height = driver.execute_script("return document.body.scrollHeight;")
    if new_height == last_height:
        break
    last_height = new_height

playlists = driver.find_elements(By.CSS_SELECTOR, 'div.playlist__meta')

for playlist in playlists:
    title = playlist.find_element(By.CSS_SELECTOR, 'h3.title').text
    hashtags = playlist.find_element(By.CSS_SELECTOR, 'p.tags').text
    like_count = playlist.find_element(By.CSS_SELECTOR, 'span.data__like-count').text
    music_count = playlist.find_element(By.CSS_SELECTOR, 'span.data__music-count').text

    ws.append([title, hashtags, like_count, music_count])

driver.quit()
wb.save('플레이리스트_정보.xlsx')