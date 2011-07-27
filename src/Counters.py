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

class Counters(db.Model):
    items_count = db.IntegerProperty(default=0)
    created = db.DateTimeProperty(auto_now_add=True)

def increase_item_counter():
    counters_db_key = db.Key.from_path("Counters", "1")
    counters_object = db.get(counters_db_key)
    if counters_object:
        counters_object.items_count+=1;
    else :
        counters_object = Counters(key_name="1",items_count=1)
    counters_object.put()
def get_item_counter():
    counters_db_key = db.Key.from_path("Counters", "1")
    counters_object = db.get(counters_db_key)
    if counters_object:
        return counters_object.items_count
    else:
        return 0