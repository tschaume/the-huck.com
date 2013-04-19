from flask import render_template
from app import app, db
from app.models import Post
import datetime

@app.route('/')
@app.route('/index')
def index():
  p = Post(title = 'first post', body = 'lorem ipsum',
           timestamp = datetime.datetime.utcnow()
          )
  db.session.add(p)
  p = Post(title = 'second post', body = 'blafasl',
           timestamp = datetime.datetime.utcnow()
          )
  db.session.add(p)
  db.session.commit()
  posts = Post.query.all()
  return render_template("index.html", posts = posts)
