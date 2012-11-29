# -*- encoding: utf-8 -*-
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
from Counters import increase_item_counter
import logging
class Index(db.Model):
    index = db.StringListProperty()
    items = db.ListProperty(db.Key)
    num_items = db.IntegerProperty(default=1)
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
        index.num_items=+1;
        index.items.append(new_item.key())
    db.put(index)

def get_items_by_search_term(search_term_list,page=0):
    indexes = db.GqlQuery("SELECT * FROM Index WHERE index = :1",search_term_list)
    items = []
    for index in indexes:
        items += index.items
    items = db.get(items[(page*10):(page+1)*10])
    return items

def get_number_of_pages(search_term_list):
    ITEMS_PAGE=10
    indexes = db.GqlQuery("SELECT * FROM Index WHERE index = :1",search_term_list)
    total_items=0
    for index in indexes:
        total_items+=len(index.items)
    if total_items>ITEMS_PAGE:
        pages=0
        if total_items%10==0:
            pages=total_items//10
        else:
            pages=(total_items//10)+1
        return total_items,pages
    return total_items,0
    

