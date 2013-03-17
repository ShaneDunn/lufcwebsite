import webapp2
import jinja2
import os
from google.appengine.ext.webapp import util

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
    def get(self, q):
        if q is None:
            q = 'index.html'
        #path = os.path.join (os.path.dirname (__file__), q)
        template = jinja_environment.get_template(q)
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([('/(.*html)?', MainPage)])
