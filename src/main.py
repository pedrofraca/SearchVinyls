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

import time
import datetime
from Search import create_search_term
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from itemsearcher import itemsearcher
from google.appengine.ext.webapp import template
from Counters import get_item_counter
from Feedback import create_feedback
import os
import PyRSS2Gen

class MainPage(webapp.RequestHandler):
    def get(self):
        template_values = {'items':get_item_counter()}
        path = os.path.join(os.path.dirname(__file__),'templates/main.html')
        self.response.out.write(template.render(path,template_values))
        
class Feedback(webapp.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__),'templates/feedback_form.html')
        self.response.out.write(template.render(path,template_values))
    def post(self):
        feedback_content=self.request.get('content')
        email=self.request.get('email')
        create_feedback(email,feedback_content)
        template_values = {'status':'Thank you so much for your feedbak. You will receive news about SearchVinyls.'}
        path = os.path.join(os.path.dirname(__file__),'templates/feedback_form.html')
        self.response.out.write(template.render(path,template_values))


class Searcher(webapp.RequestHandler):
    def get(self):
        term_to_search=self.request.get('c')
        format_=self.request.get('f')
        if self.verify(term_to_search):
            create_search_term(term_to_search)
            t0 =time.time()
            items = itemsearcher().search_items_by_string(term_to_search)
            if format_:
                if format_=='rss':
                    self.print_results_as_rss(items, term_to_search,time.time() - t0)
                else:
                    self.print_results(items, term_to_search,time.time() - t0)
            else:
                self.print_results(items, term_to_search,time.time() - t0)
        else:
            self.redirect('/')

    def print_results(self,items,searchTerm,seconds = 1):
        template_values = {
        'items_found':str(len(items)),
        'seconds':seconds,
        'search_term':searchTerm,
        'items':items}
        path = os.path.join(os.path.dirname(__file__),'templates/results.html')
        self.response.out.write(template.render(path,template_values))
    

    def print_results_as_rss(self,items,searchTerm,seconds=1):
        rss_items = []
        for item in items:
            rss_items.append(PyRSS2Gen.RSSItem(title=item.title,
                                               link=item.link,
                                               description=item.as_html(),
                                               guid = PyRSS2Gen.Guid(item.image),
                                               pubDate = datetime.datetime.now()))
        
        rss = PyRSS2Gen.RSS2(title=searchTerm,link="http://sviniyls.com",description="returned in seconds",items=rss_items)

        self.response.out.write(rss.to_xml())
        
    def verify(self,searchTerm):
        if searchTerm.strip()=='':
            return False
        return True

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/result', Searcher),
                                      ('/feedback', Feedback)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
