import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(
    "quickci-firebase-adminsdk-seay8-5f9c3c3d08.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

""" db.collection(u'users').add(
    {'email': 'tolo@test.com', 'name': 'Tolo Toleado'}) """

users_ref = db.collection(u'products')
docs = users_ref.stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
