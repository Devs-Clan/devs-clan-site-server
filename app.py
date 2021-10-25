from firebase_actions import firebase_actions
from firebase_admin import firestore
import time

def main():
    firebase = firebase_actions()
    db = firestore.client()
    while True:
        # firebase.setRequest(db,'78', 'yechiel', 'https://avatars.githubusercontent.com/u/51932344?v=4', 'making python server', 'hello, i would like to get help with a python server that i make please contact me : yechielb2000@gmail.com')
        print(firebase.verifyRequest(db, 3))
        time.sleep(300)

if __name__ == "__main__":
    main()


  