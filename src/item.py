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


class Item(db.Model):
    image = db.LinkProperty()
    links_list = db.ListProperty(db.Link)
    description = db.StringProperty()
    title = db.StringProperty()
    fromPage = db.StringProperty()
    price=db.StringProperty()
    link=""


def create_item(item_to_insert,key):
    item_db_key = db.Key.from_path("Item", key)
    item_object = db.get(item_db_key)
    if item_object:
        if not(item_object.link in item_object.links_list):
            item_object.links_list.append(db.Link(item_to_insert.link))
    else:
        item_object = Item(key_name=key,links_list = [db.Link(item_to_insert.link)],
                            image=item_to_insert.image,
                            description = item_to_insert.description,
                            fromPage = item_to_insert.fromPage,
                            price = item_to_insert.price,
                            title = item_to_insert.title)

    return item_object


