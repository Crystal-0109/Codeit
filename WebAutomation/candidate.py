import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from openpyxl import Workbook

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(3)

# 선거 웹사이트 접속
driver.get('http://info.nec.go.kr/main/showDocument.xhtml?electionId=0020240410&topMenuId=PC&secondMenuId=PCRI03')
time.sleep(1)

# '국회의원선거'탭 클릭 
driver.find_element(By.CSS_SELECTOR, '#electionId2').click()

# 서울특별시 선택
cityCode_select = Select(driver.find_element(By.CSS_SELECTOR, '#cityCode'))
# 옵션 이름으로 선택 (웹사이트에서 보이는 옵션 이름)
cityCode_select.select_by_visible_text('서울특별시')

# # 옵션의 value로 선택 ('서울특별시' 옵션의 value는 1100)
# cityCode_select.select_by_value('1100')

# # 옵션의 인덱스로 선택 ('서울특별시'는 두 번째 옵션)
# cityCode_select.select_by_index(1)

# 종로구 선택
sggCityCode_select = Select(driver.find_element(By.CSS_SELECTOR, '#sggCityCode'))
# 옵션 이름으로 선택 (웹사이트에서 보이는 옵션 이름)
sggCityCode_select.select_by_visible_text('종로구') 

# # 옵션의 value로 선택 ('종로구' 옵션의 value는 2110101)
# sggCityCode_select.select_by_value('2110101')

# # 옵션의 인덱스로 선택 ('종로구'는 두 번째 옵션)
# sggCityCode_select.select_by_index(1)

# '검색'버튼 클릭
driver.find_element(By.CSS_SELECTOR, '#spanSubmit').click()

# 필요한 국회의원 정보 가져오기


time.sleep(5)

# 웹 드라이버 종료
driver.quit()
