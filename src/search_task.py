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

from google.appengine.ext import webapp
from itemsearcher import itemsearcher
from google.appengine.ext.webapp.util import run_wsgi_app
class SearchTaskHandler(webapp.RequestHandler):
    def post(self):
        search_term = self.request.get('searchterm')
        itemsearcher().get_data_from_server_and_index_it(search_term)

application = webapp.WSGIApplication(
                                     [('/index/task', SearchTaskHandler)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()