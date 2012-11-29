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


from Search import get_five_most_search_terms
import json
import webapp2
from Search import create_search_term
from itemsearcher import itemsearcher

class MostWanted(webapp2.RequestHandler):
    def get(self):
        most_search=get_five_most_search_terms()
        json_items=[]
        for item in most_search:
            json_items.append({'item':item.searchterm})
        self.response.out.write(json.dumps({'items':json_items}))

class SearchTerm(webapp2.RequestHandler):
    def get(self):
        term_to_search=self.request.get('c')
        page=self.request.get('p')
        items_json=[]
        total=0
        pages=0
        if self.verify(term_to_search):
            create_search_term(term_to_search)
            total,pages=itemsearcher().get_number_of_pages(term_to_search)
            items = itemsearcher().search_items_by_string(term_to_search,page)
            for item in items:
                items_json.append(item.as_json())
        self.response.out.write(json.dumps({'total':total,'pages':pages,'items':items_json}))

    def verify(self,searchTerm):
        if searchTerm.strip()=='':
            return False
        return True
app = webapp2.WSGIApplication([('/api/mostwanted', MostWanted),('/api/search', SearchTerm)],debug=True)
