# Selenium 임포트
from selenium import webdriver
import time

# 크롬 드라이버 생성
driver = webdriver.Chrome()

# 사이트 접속하기
driver.get('https://codeit.kr')
# time.sleep(100)
