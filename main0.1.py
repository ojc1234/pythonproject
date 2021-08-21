from os import write
import os 
import sys 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from newscloringapi import 크롤링api
from newsdescription import 뉴스본문크롤링
from keywordcloring import 키워드크롤링
from test import 테스트
import csv
import time
from pymongo import MongoClient
import json
검색데이터크기 = 99

nowtime = time.strftime('%Y%m%d',  time.localtime(time.time())) #크롤링 구동 시간 저장
my_client = MongoClient("mongodb://localhost:27017")
mydb = my_client['cloring']
mycol = mydb['customers' + nowtime]

키워드크롤링결과 = 키워드크롤링() #빅카인즈 크롤링
rt = []
c = 0
i = 0
y =[]
p = 0
newlist = []
list = []
num = 0
twonum = 0
t = 0
st = []
for i in 키워드크롤링결과[:5]: #상위 5개의 결과
    for y in 크롤링api(i,str(검색데이터크기)):
        if (y[0].find("news.naver.com") > -1):
            rt.insert(c,y)
        
        c = c + 1
    st.insert(p,rt)
    p = p+1
print (st)


for i in st:
    twonum = 0
    for j in i:
        k= 뉴스본문크롤링(i[twonum][0],nowtime,i[twonum][1])
        time.sleep(0.5)
        print (k)
        list = []
        list.insert(num,k)
        if k.get('link') != 0:
            try:
                if not (mycol.find(i[twonum][0]) > -1):
                    mycol.update_one({"link":i[twonum][0]},{"$set":{"키워드" :mycol.find(i[twonum][0])[5]+i[twonum][1]}})
                else:
                    mycol.insert_many(list)
            except:
                mycol.insert_many(list)
        

        num = num + 1
        twonum = twonum + 1


#본문,좋아요,화나요,제목,시간