from flask import render_template
from app import app, db
from app.models import Post
import datetime
import StringIO
from asciidocapi import AsciiDocAPI
asciidoc = AsciiDocAPI()
asciidoc.options('--no-header-footer')

@app.route('/')
@app.route('/index')
@app.route('/index/<int:page>')
def index(page = 1):
  posts = Post.query.all()
  for p in posts:
    db.session.delete(p)
  db.session.commit()
  p = Post(title = 'first post', body = 'asciidoc/post.txt',
           timestamp = datetime.datetime.utcnow()
          )
  db.session.add(p)
  p = Post(title = 'second post', body = 'asciidoc/post.txt',
           timestamp = datetime.datetime.utcnow()
          )
  db.session.add(p)
  db.session.commit()
  posts = Post.query.paginate(page, 1, False) # returns Paginate object
  for p in posts.items:
    outfile = StringIO.StringIO()
    asciidoc.execute(str(p.body), outfile, backend = 'html4')
    p.body = outfile.getvalue()
  return render_template("index.html", posts = posts)
