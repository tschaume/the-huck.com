from app import db

class Post(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  body = db.Column(db.String(100), unique = True)
  timestamp = db.Column(db.DateTime)
  def __repr__(self):
    return '<Id %r,Body %r, Date %r>' % (
      self.id, self.body, self.timestamp.ctime()
    )
