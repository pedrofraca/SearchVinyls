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
import urllib

import BeautifulSoup
from BeautifulSoup import BeautifulSoup
from item import Item
          # For processing HTML


# To change this template, choose Tools | Templates
# http://www.todocoleccion.net/buscador.cfm?C=t&P=1&Bu=los%20planetas&S=t&M=t&O=r&D=t&N=i&wid=4

__author__="pfraca"
__date__ ="$Jun 2, 2011 2:17:20 PM$"

def create_headers():
    headers = {}
    #headers['Content-Type'] = 'application/x-www-form-urlencoded'
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.71 Safari/534.24'
    return headers


def get_data_from_server(string_to_search):
    h1 = httplib.HTTPConnection('www.todocoleccion.net')
    params = urllib.urlencode({'Bu':string_to_search,'P':'1','S':130000,'M':'t','O':'r','D':'t','N':'i','wid':'4'})
    h1.request("GET",'/buscador.cfm?'+params,None,create_headers())
    response = h1.getresponse();
    response_data = response.read()
    response.close();
    return response_data


def get_items(string_to_search):
    data = get_data_from_server(string_to_search)
    soup = BeautifulSoup(''.join(data))
    items = soup.findAll('a', {'class':'nombre'})
    list = []
    for theItem in items:
        newItem = Item()
        newItem.tittle=theItem.string
        newItem.fromPage="TodoColeccion"
        list.append(newItem)
    return list

