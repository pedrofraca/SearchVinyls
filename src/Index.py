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

from normalizator import normalizator
from google.appengine.ext import db
from item import create_item, Item
import copy
from Counters import increase_item_counter


class Index(db.Model):
    index = db.StringListProperty()
    items = db.ListProperty(db.Key)
    updated = db.DateTimeProperty(auto_now_add=True)

def index_item_and_store_item(item):
    item_description_mormalized = normalizator().normalize(item.title)
    phrase_encoded = normalizator().as_base_64(item_description_mormalized)
    index_db_key = db.Key.from_path("Index",phrase_encoded)
    index = db.get(index_db_key)
    if index==None:
        index = Index(key_name=phrase_encoded,index=item_description_mormalized)

    new_item = create_item(item,phrase_encoded)
    db.put(new_item)
    increase_item_counter()
    if not(new_item.key() in index.items):
        index.items.append(new_item.key())
    db.put(index)

def get_items_by_search_term(search_term_list):
    indexes = db.GqlQuery("SELECT * FROM Index WHERE index = :1",search_term_list)
    items = []
    for index in indexes:
        items += db.get(index.items)
    return expand_items(items)

def expand_items(list_to_expand):
    list_to_return = []
    for item in list_to_expand:
        if item.links_list:
            if len(item.links_list)>0:
                for link in item.links_list:
                    new_item = copy.deepcopy(item)
                    new_item.link = link
                    new_item.price = item.price_list[item.links_list.index(link)]
                    list_to_return.append(new_item)
    return list_to_return