#!env/bin/python

from app import app, db
from app.models import Post
import datetime
import argparse
from sqlalchemy.orm.exc import NoResultFound

def post(title, ascfile):
  try:
    Post.query.filter(Post.body == ascfile).one()
  except NoResultFound:
    p = Post(title = title, body = ascfile,
             timestamp = datetime.datetime.utcnow()
            )
    db.session.add(p)
    db.session.commit()
    print Post.query.get(p.id)
  else:
    print "%r already posted" % ascfile

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("title", help="post title")
  parser.add_argument("ascfile", help="asciidoc file")
  args = parser.parse_args()
  post(args.title, args.ascfile)
