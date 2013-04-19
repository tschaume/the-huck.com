from flask import render_template
from app import app, models
import datetime

@app.route('/')
@app.route('/index')
def index():
  posts = [ # fake
           models.Post(title = 'first post',
                body = 'lorem ipsum',
                timestamp = datetime.datetime.utcnow()
               ),
           models.Post(title = 'second post',
                body = 'blafasl',
                timestamp = datetime.datetime.utcnow()
               )
          ] 
  return render_template("index.html", posts = posts)
