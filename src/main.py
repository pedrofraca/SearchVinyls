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
#<div><textarea name="content" rows="3" cols="60"></textarea></div>
class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
            <head>
                <TITLE>Search for Vinyls</TITLE>
                <script type="text/javascript">
                    function f() {
                        document.forms[0][0].focus();}
                    f();</script>
            </head>
            <body>
                <center>
                    <form action="/result" method="post">
                        <img src="/images/logo.gif" alt="Big Boat" />
                        <div><h2><input name="content" maxlength="2048" type="text"/></h2></div>
                        <div><input type="submit" value="Search"></div>
                    </form>
                </center>
            </body>
          </html>""")

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
        self.response.out.write('<html  style="background-color:#FFFFFF">' +
        '<head><title>(%s) Search: %s </title> </head> <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> <body> <h2>Your search about %s has returned %s items :</h2><pre>'
        % (str(len(items)),unicode(searchTerm,'utf-8'),unicode(searchTerm,'utf-8'),str(len(items))))
        counter=1
        for item in items:
                background_row_color='#E6E6E6'
                if counter%2==0:
                    background_row_color='#FFFFFF'
                self.response.out.write('<div style=" height: 90px; background-color:%s ">' % background_row_color)
                self.response.out.write('<div id=\'data\'style="float: left; text-align: right;">')
                self.response.out.write('<h3>')
                self.response.out.write(str(counter) + '. ')
                self.response.out.write('<a href=%s style=" width:900px;">%s</a>'% (item.linkToItem,item.title))
                self.response.out.write('---->')
                self.response.out.write(item.price)
                self.response.out.write('</h3>')
                self.response.out.write('</div>')
                self.response.out.write('<div id=\'image\'style="float: right; text-align: right;">')
                if not item.image:
                    item.image = 'images/vinyl_green.png'
                self.response.out.write('<img src=%s style="width:90px; height: 90px;" ></img>' % item.image)
                self.response.out.write('</div>')
                self.response.out.write('</div>')
                
                counter=counter + 1

        self.response.out.write('</pre><script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script></body></html>')
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