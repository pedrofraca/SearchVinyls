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

import httplib
from pydoc import deque
import urllib

import BeautifulSoup
from BeautifulSoup import BeautifulSoup
from item import Item

__author__="pfraca"
__date__ ="$Jun 2, 2011 2:17:20 PM$"

def create_headers():
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.71 Safari/534.24'
    return headers


def get_data_from_server(string_to_search):
    h1 = httplib.HTTPConnection('www.discogs.com')
    params = urllib.urlencode({'q':string_to_search,'format':'Vinyl'})
    h1.request("GET",'/sell/list?'+params,None,create_headers())
    response = h1.getresponse();
    response_data = response.read()
    response.close();
    return response_data


def get_items(string_to_search):
    data = get_data_from_server(string_to_search)
    soup = BeautifulSoup(''.join(data))
    table = soup.find('table',{'class':'mpitems'})
    
    list = []
    rows = deque(table.findAll('tr'))
    rows.popleft()

    for theItem in rows:
        cols = theItem.findAll('td',recursive=False)
        newItem = Item()
        image = cols[0].find('img')
        if image:
            newItem.image=(image['src'])
        titleSpan = cols[1].find('span',{'class':'br_item_title'})
        if titleSpan:
            newItem.tittle = titleSpan.a.string
            newItem.linkToItem='http://www.discogs.com'+titleSpan.a['href']
            newItem.fromPage="Discogs"
            priceSpan = cols[4].find('span',{'class':'price'})
            if priceSpan:
                newItem.price=priceSpan.string
            list.append(newItem)

    return list

