# To change this template, choose Tools | Templates
# and open the template in the editor.

import unittest
from itemsearcher_todocoleccion import parse_data_from_server


class Todocoleccion_TestCase(unittest.TestCase):
    string_to_parse = ""
    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def test_todocoleccion_(self):
        f = open('src/todocoleccion.html')
        item = parse_data_from_server(f.read())
        self.assertEqual(item[0].fromPage,'TodoColeccion')
        self.assertEqual(item[0].price,'10,00 &euro;')
        #self.assertEqual(item[0].title,'PLANETAS - CANCIONES PARA UNA ORQUESTA QUIMICA - CD DOBLE')


if __name__ == '__main__':
    unittest.main()

