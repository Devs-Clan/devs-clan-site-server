from firebase_actions import firebase_actions
from firebase_admin import firestore

def main():
    firebase = firebase_actions()
    db = firestore.client()
    firebase.setRequest(db,'8', 'yechiel', 'https://avatars.githubusercontent.com/u/51932344?v=4', 'making python server', 'hello, i would like to get help with a python server that i make please contact me 0507177790 or yechielb2000@gmail.com')

if __name__ == "__main__":
    main()


  