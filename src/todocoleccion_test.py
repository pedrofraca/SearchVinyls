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
from itemsearcher_todocoleccion import parse_data_from_server


class Todocoleccion_TestCase(unittest.TestCase):
    string_to_parse = ""

    def test_todocoleccion_(self):
        f = open('src/todocoleccion.html')
        item = parse_data_from_server(f.read())
        self.assertEqual(item[0].fromPage,'TodoColeccion')
        self.assertEqual(item[0].price,'10,00 &euro;')
        #self.assertEqual(item[0].title,'PLANETAS - CANCIONES PARA UNA ORQUESTA QUIMICA - CD DOBLE')


if __name__ == '__main__':
    unittest.main()

