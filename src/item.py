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
import random
import copy

class Item(db.Model):
    image = db.LinkProperty()
    description = db.StringProperty()
    title = db.StringProperty()
    fromPage = db.StringProperty()
    price=db.StringProperty()
    link=db.LinkProperty()
    
    def as_html(self):
        return '<div>'+ self.title +' <strong>' + self.price_list[0] +'</strong></div><img src='+ self.image+' style="width:90px; height: 90px;" ></img>'

    def as_json(self):
        return {'title':self.title.title(),'price': self.price,'image': self.image,'link':self.link}

def create_item(item_to_insert,key):
    item_db_key = db.Key.from_path("Item", item_to_insert.link)
    item_object = db.get(item_db_key)
    if item_object:
        item_object.image=item_to_insert.image
        item_object.description=force_utf8(item_to_insert.description)
        item_object.price = force_utf8(item_to_insert.price)
        item_object.title = force_utf8(item_to_insert.title)
        item_object.fromPage = force_utf8(item_to_insert.fromPage)
    else:
        item_object = Item(key_name=item_to_insert.link,
                           link = db.Link(item_to_insert.link),
                           image=item_to_insert.image,
                           description = force_utf8(item_to_insert.description),
                           fromPage = force_utf8(item_to_insert.fromPage),
                           price = force_utf8(item_to_insert.price),
                           title = force_utf8(item_to_insert.title))
    return item_object

def force_utf8(string):
    if string != None:
        if type(string)==str:
            return string.decode('utf-8')
        else:
            return string
            
def get_four_random_items():
    q = Item.all(keys_only=True)
    item_keys = q.fetch(2000)
    if item_keys: 
        random_keys = random.sample(item_keys, 6)
        elements = db.get(random_keys)
        return elements
    return []
