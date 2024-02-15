from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/music')
time.sleep(1)

driver.execute_script("window.scrollTo(0, 200);")

scroll_height = driver.execute_script("return document.body.scrollHeight;")
print(scroll_height)