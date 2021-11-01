from firebase_actions import firebase_actions
from firebase_admin import firestore
from flask import Flask, render_template, request
from threading import Thread

firebase = firebase_actions()
db = firestore.client()
# print(firebase.verifyRequest(db, 3))

app = Flask('')

@app.route('/request')
def requestRoute():
    firebase.setRequest(db, request.args.get('rn', None),
                        request.args.get('user', None),
                        request.args.get('avatarurl', None),
                        request.args.get('highlight', None),
                        request.args.get('request', None))
    return "Request sent successfully!"

@app.route('/requests')
def requests():
    return render_template('requests.html')

@app.route('/')
def test():
    return render_template('index.html')

def run():
    app.run(host='0.0.0.0', port=5000)

def keep_alive():
    t = Thread(target=run)
    t.start()


keep_alive()
