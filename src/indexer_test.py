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

from normalizator import expand_items
class ItemMock:
    links_list = ['a','b','c']

class nomalizator_testcase(unittest.TestCase):
    string_to_parse = ""

    def test_expand_all(self):
        items_list = []
        for i in range(10):
            items_list.append(ItemMock())
        self.assertEqual(10,len(items_list))
        final_list = expand_items(items_list)
        self.assertEqual(30,len(final_list))


if __name__ == '__main__':
    unittest.main()

