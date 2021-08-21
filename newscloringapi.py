# http://ehpub.co.kr/30-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-naver-open-api-%ED%99%9C%EC%9A%A9%ED%95%98%EA%B8%B0-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0%EB%8F%84%EC%84%9C-%EA%B2%80%EC%83%89/
#제목: 네이버 검색 API 활용하기

#import
import urllib.request
import json
def 크롤링api(data,데이터크기):
    t = []
    #애플리케이션 클라이언트 id 및 secret
    client_id = "Fy8_z4m0OPjejst5H0Dl" 
    client_secret = "R5UHW9insB"
    i=0
    #도서검색 url
    #디폴트(json) https://openapi.naver.com/v1/search/book?query=python&display=3&sort=count
    #json 방식 https://openapi.naver.com/v1/search/book.json?query=python&display=3&sort=count
    #xml 방식  https://openapi.naver.com/v1/search/book.xml?query=python&display=3&sort=count
    url = "https://openapi.naver.com/v1/search/news"
    option = "&display="+데이터크기+"&sort=sim"
    query = "?query="+urllib.parse.quote(data)
    url_query = url + query + option

    #Open API 검색 요청 개체 설정
    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)

    #검색 요청 및 처리
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if(rescode == 200):  #정상적으로 호출했을때
        response_body = response.read()
        dict = json.loads(response_body)
        
    # Dictionary 데이타 체크
    for h in dict['items']:
        #print('링크' + h['link']+'   날짜 ' + h['pubDate'])
        t.insert(i, [h['link'],data])
        i = i+1
    return t
