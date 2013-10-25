activate_this = '/home/patrick/public/the-huck.com/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import logging, sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,'/home/patrick/public/the-huck.com/app')
sys.path.insert(1,'/home/patrick/public/the-huck.com')
from app import app as application
