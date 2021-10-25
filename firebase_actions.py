import firebase_admin
from firebase_admin import credentials
from datetime import datetime
from private_info import firebase_api

    
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

    def verifyRequest(self, db, request_number):
        req_ref = db.collection(u'requests')
        docs = req_ref.stream()

        for doc in docs:
            if(str(request_number) == doc.id):
                user = u'{}'.format(doc.to_dict()['user'])
                return user
        return "user not found"        
            

    def __init__(self):
        firebase_admin.initialize_app(credentials.Certificate('private_info/serviceAccountKey.json'), {
            'apiKey' : firebase_api.api_key,
            'databaseURL': 'https://devs-clan-default-rtdb.firebaseio.com'
        })



    

