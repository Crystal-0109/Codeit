from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet('코스타그램')
ws.append(['이미지 주소', '내용', '해시태그', '좋아요 수', '댓글 수'])

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/costagram/index')
time.sleep(1)

# 자동 로그인
driver.find_element(By.CSS_SELECTOR, '.top-nav__login-link').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.login-container__login-input').send_keys('codeit')
driver.find_element(By.CSS_SELECTOR, '.login-container__password-input').send_keys('datascience')
driver.find_element(By.CSS_SELECTOR, '.login-container__login-button').click()
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

### 스크롤 완료 ### 

thumbnails = driver.find_elements(By.CSS_SELECTOR, '.post-list__post')

for thumbnail in thumbnails:
    # 썸네일 클릭
    thumbnail.click()
    time.sleep(0.5)

    # 엑셀에 데이터 추가
    # 이미지 주소
    style_attr = driver.find_element(By.CSS_SELECTOR, 'div.post-container__image').get_attribute('style')
    url = style_attr.split('"')[1]
    
    # 내용
    content = driver.find_element(By.CSS_SELECTOR, 'span.content__text').text.strip()

    # 해시태그
    hashtags = driver.find_element(By.CSS_SELECTOR, 'div.content__tag-cover').text.strip()

    # 좋아요 수
    like_count = driver.find_element(By.CSS_SELECTOR, 'span.content__like-count').text.strip()

    # 댓글 수
    comment_count = driver.find_element(By.CSS_SELECTOR, 'span.content__comment-count').text.strip()

    ws.append([url, content, hashtags, like_count, comment_count])
    
    # 닫기 버튼 클릭
    driver.find_element(By.CSS_SELECTOR, 'button.close-btn').click()
    time.sleep(0.5)

driver.quit()

wb.save('코스타그램.xlsx')