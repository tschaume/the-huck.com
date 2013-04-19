from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  posts = [ # fake
           { 'title': 'first post', 'body': 'lorem ipsum' },
           { 'title': 'second post', 'body': 'blafasl' }
          ] 
  return render_template("index.html", posts = posts)
