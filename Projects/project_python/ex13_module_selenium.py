#selenium : 사용자가 브라우저 (크롬 , 엣지) 에서 수행하는 행동을 싸이썬 코드가 대신 움직이도록 해 주는 모듈
# -웰 크롤링(러) or RPA 자동화서비스 개발에 활용 robotics processing automation : 자동으로 알아서 처리하는 프로그램 

# 0 모듈 설치 
# pip install selenium , pip list , exit

#1. 모듈 사용
import time 

from selenium import webdriver 
# 웹 드라이버 : 웹 브라우저를 제어하는 프로그램  : 구글에서 웹드라이버 

from selenium.webdriver.common.by import By # by : ~에 의하여 find 하겠다. 


#2. 크롬을 제어하는 웹 드라이버 준비
chrome = webdriver.Chrome()
chrome.get('https://www.naver.com')

#바로 꺼지니까... 잠시 대기 ... 그래서 time 모듈을 위에 넣음.

time.sleep(5)

#셀레니움으로 웹브라우저에 사람이 하는 행동을 대신 요청 !!!
#3. 네이버의 검색어 읿력창을 찾기 

# 네이버의 검색창에 오른쪽 클릭해서 검사를 하면 해당 창의 코드가 보이고 거기에 class가 보임. 
search_box = chrome.find_element(By.CLASS_NAME,"search_input") # By.CLASS XX
#키보드값 입력
search_box.send_keys('스타벅스')

#바로 꺼지니까... 잠시 대기 ... 그래서 time 모듈을 위에 넣음.

time.sleep(5)

#4. 검색버튼 찾아서 클릭
# 검색창 옆에 돋보기를 클릭해야 하는데.. 이 그림을 오늘쪽 클릭 하면 검사 가 있는데 이것을 보면 해당 영역의 코드를 보는데 거기에 svg : scale vector graphic이 
# 있는데 이것을 감싼 버튼의 id를 찾아 클릭하게 제어해야 함. 
search_button = chrome.find_element(By.ID,"search-btn")
search_button.click()
#바로 꺼지니까... 잠시 대기 ... 그래서 time 모듈을 위에 넣음.

time.sleep(5)

#파이썬을 이용해서 자동화 프로그램을 만들수 있음.. 해킹처럼....

# 내가 원하는 것을 자동으로 하기 위해서 파이썬이 필요함... 
# flask는 나의 컴퓨터가 웹서버가 되게 하는 방법. 




