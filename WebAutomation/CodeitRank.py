from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(3)

driver.get('https://www.codeit.kr/signin')
time.sleep(1)

# 자동 로그인
driver.find_element(By.CSS_SELECTOR, '.inputField_input__004jm.inputField_withLabel__z5_la').send_keys('aaaa@naver.com') # 이메일 입력
driver.find_element(By.NAME, 'password').send_keys('aaaa') # 비밀번호 입력
driver.find_element(By.CSS_SELECTOR, '.Button_button___Dadr.Button_primary__BxDoK.Button_fullWidth__Wp545').click()  # 로그인
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.Button_button___Dadr.Button_primary__BxDoK.Button_medium__BjTrN').click()  # 캠프 시작하기 버튼 누르기

# 수강 랭킹
for i in range(3):
    rank = driver.find_elements(By.CSS_SELECTOR, '.RankBoard_order__J2PYl')[i].text.strip()
    xp = driver.find_elements(By.CSS_SELECTOR, '.Ranking_xp__pP3d_')[i].text.strip()
    name = driver.find_elements(By.CSS_SELECTOR, '.RankBoard_name__Lm7TB')[i].text.strip()
    
    xp = ''.join(filter(str.isdigit, xp))

    print(f"{rank} {xp} {name}")

time.sleep(10)

driver.quit()