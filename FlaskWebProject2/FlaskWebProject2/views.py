"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template , render_template, redirect, request, url_for
from FlaskWebProject2 import app
from pymongo import MongoClient
i = 0
p = []
q = 0
client = MongoClient('mongodb://localhost:27017/')
db = client.hello
collection = db["customers2021-07-13"]
키워드목록 = collection.find({"키워드":"경기"})


@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='개발자 정보'
    )

@app.route('/copyright')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='Copyright',
        year=datetime.now().year,
        message='어플 저작권'
    )
@app.route('/')
@app.route('/mongo',methods=['GET'])
def mongoTest():
    global i,p,q
    i = 0
    p = []
    q = 0
    j = 0
    t = 0
    u= 0
    a = 0
    k = []
    client = MongoClient('mongodb://localhost:27017/')
    db = client.hello
    newcollection = db.collection_names(include_system_collections=False)
    #likeadd = newcollection.find("like")
    for i in newcollection:
        p.insert(q,i)
        q=q+1

        
        
    return render_template('mongo.html', date=p ,i = 0,title='mongo',year=datetime.now().year,message='Your application description page.')
@app.route('/mongo/<date>')
def mongodata(date):
    client = MongoClient('mongodb://localhost:27017/')
    db = client.hello
    collection = db[date]
    # 새로운결과=db.find()
    t = 0
    p = 0
    키워드목록 = collection.find()
    results = collection.find()
    newlike = collection.find()
    for i in newlike:
        t = t +  int(i.get("like"))
        p = p + int(i.get("angry"))
    return render_template('main.html', data=results,keyword=키워드목록,today=date,title='About',year=datetime.now().year,message='Your application description page.',likeadd = t,angryadd=p)