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
from google.appengine.api import memcache
from Index import index_item_and_store_item
from google.appengine.ext.webapp.util import run_wsgi_app

class IndexTaskHandler(webapp.RequestHandler):
    def post(self):
        all_items = memcache.get("items")
        if all_items:
            for item in all_items:
                index_item_and_store_item(item)

application = webapp.WSGIApplication(
                                     [('/index/index', IndexTaskHandler)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()