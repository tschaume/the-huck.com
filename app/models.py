from app import db

class Post(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(120))
  body = db.Column(db.String(100), unique=True)
  timestamp = db.Column(db.DateTime)
  def __repr__(self):
    return '<Id %r, Title %r, Body %r, Date %r>' % (
      self.id, self.title, self.body, self.timestamp.ctime()
    )
