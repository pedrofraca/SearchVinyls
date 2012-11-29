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

import itemsearcher_discogs
import itemsearcher_todocoleccion

from Index import get_items_by_search_term,get_number_of_pages , index_item_and_store_item
from normalizator import normalizator
from google.appengine.api import memcache
from google.appengine.api import taskqueue
class itemsearcher:
    def search_items_by_string(self,text,page=0):
        if page=='' or page ==None or page=='0':
            page=0
        else:
            page=int(page)-1
            
        text_normalized = normalizator().normalize(text)
        all_items = get_items_by_search_term(text_normalized,page)
        if all_items==None:
            self.get_data_from_server_and_store_it(text)
            all_items = get_items_by_search_term(text_normalized)
        if len(all_items)<5 and page==0:
            self.get_data_from_server_and_store_it(text)
            all_items = get_items_by_search_term(text_normalized)
        return all_items
    
    def get_number_of_pages(self,text):
        text_normalized = normalizator().normalize(text)
        return get_number_of_pages(text_normalized)
    
    def get_data_from_server_and_store_it(self,text):
            items_discogs = itemsearcher_discogs.get_items(text)
            items_todo_coleccion = itemsearcher_todocoleccion.get_items(text)
            all_items = items_discogs + items_todo_coleccion
            for item in all_items:
                index_item_and_store_item(item)
            
    def get_data_from_server_and_index_it(self,text):
            items_discogs = itemsearcher_discogs.get_items(text)
            items_todo_coleccion = itemsearcher_todocoleccion.get_items(text)
            all_items = items_discogs + items_todo_coleccion
            memcache.add("items", all_items, 60)
            taskqueue.add(url='/index/index',params={})
            return all_items
