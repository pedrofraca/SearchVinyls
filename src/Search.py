from google.appengine.ext import db
class Search(db.Model):
    searchterm = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)

    def create(self):
        self.put()
