import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

project_id = 'tareas-flask'
credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential,{
    'projectId':project_id,
})

db = firestore.client()


def get_users():
    return db.collection('user').get()


def get_user(user_id):
    return db.collection('user').document(user_id).get()


def user_put(user_data):
    user_ref = db.collection('user').document(user_data.username)
    user_ref.set({'password':user_data.password})


def get_todos(user_id):
    return db.collection('user')\
        .document(user_id)\
        .collection('todos').get()


def put_todo(user_id, description):
    todos_collection_ref = db.collection('user').document(user_id).collection('todos')
    todos_collection_ref.add({'description': description, 'done':False})

def delete_todo(user_id, todo_id):
    todo_ref = db.document('user/{}/todos/{}'.format(user_id,todo_id))
    todo_ref.delete()
    #todo_fef = db.collection('user').document(user_id).collection('todos').document(todo_id)