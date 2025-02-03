import firebase_admin
from firebase_admin import credentials, firestore, db

cred = credentials.Certificate('interactive-quiz-applica-ff179-firebase-adminsdk-15y82-158895a097.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def store_result(user_id, score, total):
    data = {
        'user_id': user_id,
        'score': score,
        'total': total
    }
    db.collection('quiz_results').add(data)
