#Ch_selenium/example/tutorial4.py
from selenium import webdriver
import time
characters = "[]"
def 뉴스본문크롤링(link,nowtime,keyword):
    driver = webdriver.Chrome('chromedriver.exe') #또는 chromedriver.exe
    driver.implicitly_wait(15) # 묵시적 대기, 활성화를 최대 15초가지 기다린다.
    뉴스본문 = []
    # 페이지 가져오기(이동)
    driver.get(link)
    time.sleep(1)
    # 요소 찾기 - 검색창찾고 키 전송
    try:
        try:
            string = driver.find_element_by_id("articleBodyContents").text
            for x in range(len(characters)):
                string = string.replace(characters[x],"")

            뉴스본문.insert(0, string)
        except Exception:
            string = driver.find_element_by_id("newsEndContents").text
            
            for x in range(len(characters)):
                string = string.replace(characters[x],"")

            뉴스본문.insert(0, string)
        time.sleep(0.2)

        locates='li.u_likeit_list.good > a > span.u_likeit_list_count._count'
        elements=driver.find_elements_by_css_selector(locates)
        뉴스본문.insert(1, elements[1].text)

        locates='li.u_likeit_list.angry > a > span.u_likeit_list_count._count'
        elements=driver.find_elements_by_css_selector(locates)
        뉴스본문.insert(2, elements[1].text)
        time.sleep(0.2)
        try:
            locates='div.article_info > div > span'
            elements=driver.find_elements_by_css_selector(locates)
            뉴스본문.insert(3, elements[0].text)
            time.sleep(0.2)
        except Exception:
            locates='div.news_headline > div > span:nth-child(1)'
            elements=driver.find_elements_by_css_selector(locates)
            뉴스본문.insert(3, elements[0].text)
            time.sleep(0.2)
        
        try:
            locates='#articleTitle'
            elements=driver.find_elements_by_css_selector(locates)
            뉴스본문.insert(4, elements[0].text)
            time.sleep(0.2)
            
        except Exception:
            locates='div.news_headline > h4'
            elements=driver.find_elements_by_css_selector(locates)
            뉴스본문.insert(4, elements[0].text)
            time.sleep(0.2)


        뉴스본문.insert(5, link)
        뉴스본문.insert(6, nowtime)
        뉴스본문.insert(7, keyword)
    except Exception:
        뉴스본문 = [0,0,0,0,0,0,0]
    time.sleep(0.5)
    print (뉴스본문)

    mylist = {
    'des': 뉴스본문[0],
    'like': 뉴스본문[1],
    'angry':뉴스본문[2],
    'time':뉴스본문[3],
    'title':뉴스본문[4],
    'link' :뉴스본문[5],
    'refreshtime':뉴스본문[6],
    '키워드':뉴스본문[7]
    }

    return mylist
