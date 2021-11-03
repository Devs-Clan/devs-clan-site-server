from firebase_actions import firebase_actions
from firebase_admin import firestore
from flask import Flask, render_template, request
from threading import Thread
from github_actions import github_actions

firebase = firebase_actions()
db = firestore.client()
# print(firebase.verifyRequest(db, 3))

g = github_actions()


app = Flask('')

@app.route('/request')
def requestRoute():

    memberInfo = g.getMemberInfo(memberName=request.args.get('user', None))

    firebase.setRequest(db, request.args.get('rn', None),
                        memberInfo['user'],
                        memberInfo['avatarurl'],
                        request.args.get('highlight', None),
                        request.args.get('request', None))
    return "We have sent your request " + str(memberInfo['user']) + ". Please return to requests section."

@app.route('/')
def test():
    return render_template('index.html')

def run():
    app.run(host='0.0.0.0', port=5000)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()
