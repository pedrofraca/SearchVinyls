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

import unittest

from normalizator import normalizator


class nomalizator_testcase(unittest.TestCase):
    string_to_parse = ""

    def test_normalize_string_returns_list(self):
        the_normalizator = normalizator()
        result=[]
        result = the_normalizator.normalize("los planetas")
        self.assertEqual(len(result), 1)
    def test_normalize_string_resturns_correct_array(self):
        the_normalizator = normalizator()
        result=[]
        result = the_normalizator.normalize("los planetas")
        self.assertEqual(result[0], "planetas")
    def test_normalize_string_avoids_articles(self):
        the_normalizator = normalizator()
        result = the_normalizator.normalize("el fary")
        self.assertEqual(result[0], "fary")
    def test_normalize_string_avoids_some_articles(self):
        the_normalizator = normalizator()
        result = the_normalizator.normalize("el fary los planetas")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "fary")
        self.assertEqual(result[1], "planetas")
    def test_normalize_string_avoids_some_articles_and_uppercase(self):
        the_normalizator = normalizator()
        result = the_normalizator.normalize("el Fary LOS PLANETAS")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "fary")
        self.assertEqual(result[1], "planetas")
    def test_normalize_string_avoids_some_articles_languages(self):
        the_normalizator = normalizator()
        result = the_normalizator.normalize("the red hot chili peepers")
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], "red")
        self.assertEqual(result[1], "hot")
        self.assertEqual(result[2], "chili")
        self.assertEqual(result[3], "peepers")


if __name__ == '__main__':
    unittest.main()

