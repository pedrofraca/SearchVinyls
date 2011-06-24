from Search import Search
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
                        <img src="/images/logo.png" alt="Big Boat" />
                        <div><h2><input name="content" maxlength="2048" type="text"/></h2></div>
                        <div><input type="submit" value="Search"></div>
                    </form>
                </center>
            </body>
          </html>""")
class Searcher(webapp.RequestHandler):
    def post(self):
        toSearch=self.request.get('content')
        toSearch = toSearch.encode('utf-8')
        searchTerm = Search(searchterm=toSearch)
        searchTerm.create()
        items = itemsearcher().search_items_by_string(toSearch)
        self.response.out.write('<html> <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> <body><h2>Your search about %s has returned %s items :</h2><pre>' % (unicode(toSearch,'utf-8'),str(len(items))))
        counter=1
        for item in items:
                self.response.out.write('<div>')
                self.response.out.write('<h3>')
                self.response.out.write(str(counter) + '. ')
                self.response.out.write(item.tittle)
                self.response.out.write('---->')
                self.response.out.write(item.price)
                self.response.out.write('</h3>')
                self.response.out.write(item.image)
                self.response.out.write('</div>')
                counter=counter + 1

        self.response.out.write('</pre></body></html>')

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/result', Searcher)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()