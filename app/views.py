from flask import render_template
from app import app, db
from app.models import Post
import StringIO
from sqlalchemy import desc
from asciidocapi import AsciiDocAPI
asciidoc = AsciiDocAPI()
asciidoc.options('--no-header-footer')
import os

def run_asciidoc(p):
  outfile = StringIO.StringIO()
  asciidoc.execute(str(p.body), outfile, backend = 'html4')
  return outfile.getvalue()

@app.route('/')
@app.route('/index')
@app.route('/index/<int:page>')
def index(page = 1):
  posts = Post.query.order_by(desc(Post.timestamp)).paginate(page, 1, False)
  for p in posts.items:
    p.body = run_asciidoc(p)
  return render_template("index.html", posts = posts)

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/news')
def news():
  return render_template("news.html")

@app.route('/science')
def science():
  return render_template("science.html")

@app.route('/archive')
def archive():
  return render_template("archive.html", posts = Post.query.all())

@app.route('/archive/<int:id>')
def post(id = 1):
  post = Post.query.get(id)
  post.body = run_asciidoc(post)
  return render_template("posts.html", post = post)

@app.route('/tweets')
def tweets():
  return render_template("tweets.html")

@app.route('/repos')
def repos():
  return render_template("repos.html")

@app.errorhandler(500)
def internal_error(exception):
  app.logger.exception(exception)
  return render_template('500.html'), 500

@app.context_processor
def my_util_processor():
  def get_post_title(url):
    base = os.path.basename(url)
    return os.path.splitext(base)[0]
  return dict(get_post_title = get_post_title)
