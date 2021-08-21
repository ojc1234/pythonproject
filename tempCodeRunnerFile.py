@app.route('/mongo/<data>',methods=['GET'])
def mongoTest(data):
    client = MongoClient('mongodb://localhost:27017/')
    db = client.cloring
    collection = db["customers"+data]
    키워드목록 = collection.find({"키워드":"경기"})
    results = collection.find()
    client.close()
    return render_template('main.html', data=results,keyword=키워드목록)