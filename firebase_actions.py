import firebase_admin
from firebase_admin import credentials
from datetime import datetime
    
class firebase_actions:

    def setRequest(self, db, request_number, user, user_icon, highlight, request):
        doc_ref = db.collection(u'requests').document(request_number)
        doc_ref.set({
            u'user': user,
            u'user_icon': user_icon,
            u'highlight': highlight,
            u'request': request,
            u'time': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })

    def verifyRequest(self, db):
        req_ref = db.collection(u'requests')
        docs = req_ref.stream()

        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')
            

    def __init__(self):
        firebase_admin.initialize_app(credentials.Certificate('secrets/serviceAccountKey.json'), {
            'apiKey' : "AIzaSyBtUcu3gpNGV0ReN7fklRDOY7QwOtTGEAg",
            'databaseURL': 'https://devs-clan-default-rtdb.firebaseio.com'
        })



    

