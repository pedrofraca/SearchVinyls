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

import string
import base64
class normalizator():
    def remove_words_in_list(self,words_to_remove,list):
        for word in list:
            for remove_word in words_to_remove:
                if word == remove_word:
                    list.remove(word)
        return list

    def normalize(self,string_to_normalize):
        articles = ['el','la','los','las','un','una','unos','unas','lo','al','del','the']
        string_to_normalize = string.lower(string_to_normalize)
        return self.remove_words_in_list(articles,string_to_normalize.split(' '))

    def as_base_64(self,words_list):
        phrase=""
        for word in words_list:
            phrase += word
            phrase_encoded = base64.b64encode(phrase.encode('utf-8'))
        return phrase_encoded