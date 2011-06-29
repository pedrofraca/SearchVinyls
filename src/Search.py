#   This file is part of SearchVinyls.
#
#    SearchVinyls is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Foobar is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

from google.appengine.ext import db
class Search(db.Model):
    searchterm = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    times = db.IntegerProperty(default=1)

def create_search_term(searchterm):
    searchterm = searchterm.lower()
    searchterm = searchterm.decode('utf-8')
    search_db_key = db.Key.from_path("Search", searchterm)
    search_term_object = db.get(search_db_key)
    if(search_term_object):
        search_term_object.times+=1;
    else :
        search_term_object = Search(key_name=searchterm,searchterm=searchterm)
    search_term_object.put()
