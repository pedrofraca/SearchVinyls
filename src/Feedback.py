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
from google.appengine.api import mail

class Feedback(db.Model):
    email = db.StringProperty()
    feedback = db.StringProperty(multiline=True)
    created = db.DateTimeProperty(auto_now_add=True)

def create_feedback(email,feedback):
    feedback_object = Feedback(email=email,feedback=feedback)
    feedback_object.put()
    mail.send_mail(sender="Pedro Fraca <pedro.fraca@gmail.com>",
              to="<pedro.fraca@gmail.com>",
              subject="Feedback from searchvinyls",
              body=" A new feedback message from " + email +" has been created :" + feedback)
