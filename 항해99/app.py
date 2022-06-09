from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://taesikyoon97:louis17467@cluster0.ncjxm.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    #post 할때는 db등록하고 db넣고 하는거였음 post 방식으로 등록 및 추가??
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]
    doc= {
        'name': name_receive,
        'comment': comment_receive
    }
    db.fans.insert_one(doc)

    return jsonify({'msg':'응원 남기기 완료'})

@app.route("/homework", methods=["GET"])
def homework_get():
    #get 은 데이터 베이스 정보를 받아와서 보여주는거였는데 그래서 데이터 베이스에서 찾아오고
    fans_cheerup = list(db.fans.find({}, {'_id': False}))
    return jsonify({'fans':fans_cheerup})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
