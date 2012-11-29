#   This file is part of SearchVinyls.
#
#    SearchVinyls is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    SearchVinyls is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with SearchVinyls.  If not, see <http://www.gnu.org/licenses/>.

from google.appengine.ext import db
from google.appengine.api import taskqueue
import logging
class Search(db.Model):
    searchterm = db.StringProperty()
    created = db.DateTimeProperty(auto_now=True)
    times = db.IntegerProperty(default=1)

def create_search_term(searchterm):
    searchterm = searchterm.lower()
    search_db_key = db.Key.from_path("Search", searchterm)
    search_term_object = db.get(search_db_key)
    if(search_term_object):
        search_term_object.times+=1;
    else :
        search_term_object = Search(key_name=searchterm,searchterm=searchterm)
    search_term_object.put()

def get_five_most_search_terms():
    q = Search.all().order('-times')
    elements = q.fetch(5)
    new_element=[]
    for element in elements:
        element.searchterm=element.searchterm.title()
        new_element.append(element)
    return new_element

    
def generate_tasks_for_all_search_terms():
    search_terms = Search.all()
    for search in search_terms:
        taskqueue.add(url='/index/task',params={'searchterm':search.searchterm})

