from google.appengine.ext import db
class Search(db.Model):
    searchterm = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    times = db.IntegerProperty(default=1)

def create_search_term(searchterm):
    search_db_key = db.Key.from_path("Search", searchterm)
    search_term_object = db.get(search_db_key)
    if(search_term_object):
        search_term_object.times+=1;
    else :
        search_term_object = Search(key_name=searchterm,searchterm=searchterm)
    search_term_object.put()
