import firebase_admin
from firebase_admin import credentials, firestore

# Firebase will automatically handle the PEM formatting inside the JSON file
cred = credentials.Certificate('C:\\Users\\KIIT0001\\projects\\test-yt-ai\\backend\\firebase-config.json')
firebase_admin.initialize_app(cred)

firebase_db = firestore.client()