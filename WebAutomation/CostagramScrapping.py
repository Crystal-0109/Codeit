from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook
from bs4 import BeautifulSoup

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

thumbnails = driver.find_elements(By.CSS_SELECTOR, 'div.post-list__post.post')

for thumbnail in thumbnails:
    # driver.find_element(By.CSS_SELECTOR, 'post-list__post').click()
    thumbnail.click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'button.close-btn').click()
    time.sleep(0.5)

driver.quit()
