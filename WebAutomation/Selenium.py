from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome() 
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/costagram/index')
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.top-nav__login-link').click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.login-container__login-input').send_keys('codeit')
driver.find_element(By.CSS_SELECTOR, '.login-container__password-input').send_keys('datascience')
driver.find_element(By.CSS_SELECTOR, '.login-container__login-button').click()

time.sleep(10)