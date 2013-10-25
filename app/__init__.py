from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

#if app.debug is not True:
#  import logging
#  from logging.handlers import RotatingFileHandler
#  outfile = '/home/patrick/public/the-huck.com/public/python.log'
#  file_handler = RotatingFileHandler(outfile, maxBytes=1024 * 1024 * 100, backupCount=20)
#  file_handler.setLevel(logging.ERROR)
#  app.logger.addHandler(file_handler)
