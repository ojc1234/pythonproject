from flask import Flask, render_template, redirect, request, url_for
from pymongo import MongoClient
import json
i = 0
p = []
q = 0
client = MongoClient('mongodb://localhost:27017/')
db = client.cloring
collection = db["customers2021-07-13"]
키워드목록 = collection.find({"키워드":"경기"})
app = Flask(__name__)
@app.route('/')
    
@app.route('/mongo',methods=['GET'])
def mongoTest():
    global i,p,q
    i = 0
    p = []
    q = 0
    client = MongoClient('mongodb://localhost:27017/')
    db = client.cloring
    newcollection = db.collection_names(include_system_collections=False)
    for i in newcollection:
        p.insert(q,i)
        q=q+1
    client.close()
    return render_template('mongo.html', date=p ,i = 0)
@app.route('/mongo/<date>',)
def mongodata(date):

    client = MongoClient('mongodb://localhost:27017/')
    db = client.cloring
    collection = db[date]
    # 새로운결과=db.find()
    키워드목록 = collection.find()
    results = collection.find()
    client.close()
    return render_template('main.html', data=results,keyword=키워드목록,today=date)
if __name__ == '__main__':
    app.run(debug=True)

