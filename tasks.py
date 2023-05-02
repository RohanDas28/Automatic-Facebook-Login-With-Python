from celery import Celery
import os, sys
sys.path.append(os.getcwd())
import facebook
app = Celery('tasks', broker='redis://localhost', backend='redis://localhost')

@app.task
def sign_up(user_data):
    fb = facebook.Facebook()
    fb.sign_up(user_data)
    return user_data

@app.task
def add(x,y):
    return x+y

