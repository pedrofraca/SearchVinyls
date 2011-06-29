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

import itemsearcher_discogs
import itemsearcher_todocoleccion
class itemsearcher:
    def search_items_by_string(self,text):
        items_discogs = itemsearcher_discogs.get_items(text)
        items_todo_coleccion = itemsearcher_todocoleccion.get_items(text)
        return items_discogs + items_todo_coleccion