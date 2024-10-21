# host.py
import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, render_template, request, redirect

# Initialize the Firebase database
cred = credentials.Certificate("C:/Users/conno/OneDrive/Documents/BYUI/Fall - 2024/CSE310/TaskMaster02/clouddatabase---connor-babb-firebase-adminsdk-4v3kf-5fe5ca78d1.json")
firebase_admin.initialize_app(cred)

# creates client db to interact with the database
db = firestore.client()

# Functions to do things to tasks on the website
def add_task_db(user_id, task_name, due_date):
    task_ref = db.collection('users').document(user_id).collection('tasks').document()
    task_ref.set({
        'name': task_name,
        'due_date': due_date,
        'completed': False
    })
    print(f'Task {task_name} added with due date {due_date}!')

def edit_task_db(user_id, task_id, new_data):
    task_ref = db.collection('users').document(user_id).collection('tasks').document(task_id)
    task_ref.update(new_data)
    print(f'Task {task_id} updated!')

def delete_task_db(user_id, task_id):
    task_ref = db.collection('users').document(user_id).collection('tasks').document(task_id)
    task_ref.delete()
    print(f'Task {task_id} deleted!')

def list_tasks(user_id):
    tasks = db.collection('users').document(user_id).collection('tasks').stream()
    tasks_dict = {}

    for task in tasks:
        task_data = task.to_dict()
        tasks_dict[task.id] = {
            'name': task_data['name'],
            'due_date': task_data['due_date'],
            'completed': task_data['completed']
        }
    
    return tasks_dict

# Initialize Flask app
app = Flask(__name__)

# Routes to display tasks/edit/add/delete tasks
@app.route('/')
def home():
    tasks = list_tasks(user_id='connor_babb')
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form['task_name']
    due_date = request.form['due_date']
    add_task_db(user_id='connor_babb', task_name=task_name, due_date=due_date)
    return redirect('/')

@app.route('/edit/<task_id>', methods=['POST'])
def edit_task(task_id):
    task_name = request.form['task_name']
    due_date = request.form['due_date']
    edit_task_db(user_id='connor_babb', task_id=task_id, new_data={'name': task_name, 'due_date': due_date})
    return redirect('/')

@app.route('/delete/<task_id>', methods=['POST'])
def delete_task(task_id):
    delete_task_db(user_id='connor_babb', task_id=task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
