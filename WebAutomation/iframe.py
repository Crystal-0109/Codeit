from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(3)

# 코드잇 네이버 블로그 접속
driver.get('https://blog.naver.com/codeitofficial')
time.sleep(1)

# 'mainFrame'으로 이동
driver.switch_to.frame('mainFrame')

# 블로그 글 내용 출력
print(driver.find_element(By.CSS_SELECTOR, 'div.se-main-container').text)

driver.quit()
