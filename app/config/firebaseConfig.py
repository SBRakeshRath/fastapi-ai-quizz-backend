import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os
import json
load_dotenv()



firebase_credentials_json = os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY")

# Firebase will automatically handle the PEM formatting inside the JSON file
cred = credentials.Certificate(json.loads(firebase_credentials_json))
firebase_admin.initialize_app(cred)

firebase_db = firestore.client()