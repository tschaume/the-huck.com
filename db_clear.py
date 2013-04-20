#!env/bin/python

from app import app, db
from app.models import Post

posts = Post.query.all()
for p in posts:
  db.session.delete(p)
db.session.commit()
print Post.query.all()
