from flask import render_template
from app import app, db
from app.models import Post
import StringIO
from asciidocapi import AsciiDocAPI
asciidoc = AsciiDocAPI()
asciidoc.options('--no-header-footer')

@app.route('/')
@app.route('/index')
@app.route('/index/<int:page>')
def index(page = 1):
  posts = Post.query.paginate(page, 1, False) # returns Paginate object
  for p in posts.items:
    outfile = StringIO.StringIO()
    asciidoc.execute(str(p.body), outfile, backend = 'html4')
    p.body = outfile.getvalue()
  return render_template("index.html", posts = posts)

@app.route('/about')
def about():
  return render_template("about.html")
