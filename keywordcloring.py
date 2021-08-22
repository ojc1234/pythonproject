from selenium import webdriver
import time
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--headless')

chrome_options.add_argument('--no-sandbox')

chrome_options.add_argument('--disable-dev-shm-usage')
options = webdriver.ChromeOptions()
def 키워드크롤링():
    driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chrome_options) #또는 chromedriver.exe
    driver.implicitly_wait(15) # 묵시적 대기, 활성화를 최대 15초가지 기다린다.
    # 페이지 가져오기(이동)
    driver.get('https://www.bigkinds.or.kr/')
    #Ch_selenium/example/tutorial4.py
    str = []
    time.sleep(3)
    # 요소 찾기 - 검색창찾고 키 전송
    str = driver.find_element_by_id("category-keyword-all").text
    str = str.split('\n')
    time.sleep(0.2)
    #driver.find_element_by_id("sidolabel").click()
    time.sleep(0.2)
    return str
print (키워드크롤링())
