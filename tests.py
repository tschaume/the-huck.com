#!env/bin/python
import os
import unittest
import datetime

from config import basedir
from app import app, db
from app.models import Post

class TestCase(unittest.TestCase):
  def setUp(self):
    app.config['TESTING'] = True
    app.config['CSRF_ENABLED'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
    self.app = app.test_client()
    db.create_all()

  def tearDown(self):
    db.session.remove()
    db.drop_all()

  def test_post(self):
    pi = Post(title = 'test post', body = 'lorem ipsum',
             timestamp = datetime.datetime.utcnow()
            )
    db.session.add(pi)
    db.session.commit()
    po = Post.query.get(1)
    print pi.title, po.title
    assert pi.title == po.title

if __name__ == '__main__':
  unittest.main()
