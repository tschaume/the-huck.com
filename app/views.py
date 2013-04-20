from flask import render_template
from app import app, db
from app.models import Post
import datetime

@app.route('/')
@app.route('/index')
@app.route('/index/<int:page>')
def index(page = 1):
  posts = Post.query.all()
  for p in posts:
    db.session.delete(p)
  db.session.commit()
  p = Post(title = 'first post', body = 'lorem ipsum',
           timestamp = datetime.datetime.utcnow()
          )
  db.session.add(p)
  p = Post(title = 'second post', body = 'blafasl',
           timestamp = datetime.datetime.utcnow()
          )
  db.session.add(p)
  db.session.commit()
  posts = Post.query.paginate(page, 1, False)
  return render_template("index.html", posts = posts)
