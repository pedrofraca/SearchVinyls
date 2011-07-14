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

from Search import create_search_term
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from itemsearcher import itemsearcher
from google.appengine.ext.webapp import template
import os
#<div><textarea name="content" rows="3" cols="60"></textarea></div>
class MainPage(webapp.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__),'templates/main.html')
        self.response.out.write(template.render(path,template_values))

class Searcher(webapp.RequestHandler):
    def post(self):
        term_to_search=self.request.get('content')
        term_to_search = term_to_search.encode('utf-8')
        if self.verify(term_to_search):
            create_search_term(term_to_search)
            items = itemsearcher().search_items_by_string(term_to_search)
            self.print_results(items, term_to_search)
        else:
            self.redirect('/')

    def print_results(self,items,searchTerm):
        template_values = {
        'items_found':str(len(items)),
        'search_term':unicode(searchTerm,'utf-8'),
        'items':items}
        path = os.path.join(os.path.dirname(__file__),'templates/results.html')
        self.response.out.write(template.render(path,template_values))

        
    def verify(self,searchTerm):
        if searchTerm.strip()=='':
            return False
        return True

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/result', Searcher)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()