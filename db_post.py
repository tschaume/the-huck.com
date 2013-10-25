#!env/bin/python

from app import app, db
from app.models import Post
import datetime
import argparse
from sqlalchemy.orm.exc import NoResultFound
import os

def post(ascfile):
  try:
    pq = Post.query.filter(Post.body == ascfile)
    pq.one()
  except NoResultFound:
    post = Post(body = os.path.abspath(ascfile), timestamp = datetime.datetime.utcnow())
    print "add %r" % post
    db.session.add(post)
    db.session.commit()
    print Post.query.get(post.id)
  else:
    print "%r already posted" % ascfile
    #print "updating timestamp ..."
    #for p in pq.all():
    #  p.timestamp = datetime.datetime.utcnow()
    #  print Post.query.get(p.id)
    #db.session.commit()

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("ascfile", help="asciidoc file")
  args = parser.parse_args()
  post(args.ascfile)
