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


import httplib
import urllib
import logging
from bs4 import BeautifulSoup
import html5lib
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
    params = urllib.urlencode({'Bu':string_to_search.encode('utf-8'),'P':'1','S':130000,'M':'t','O':'r','D':'t','N':'i','wid':'4'})
    h1.request("GET",'/buscador.cfm?'+params,None,create_headers())
    response = h1.getresponse();
    response_data = response.read()
    response.close();
    return response_data


def get_items(string_to_search):
    data = get_data_from_server(string_to_search)
    if data:
        return parse_data_from_server(data)
    return []

def parse_data_from_server(html_data):
    soup = BeautifulSoup(html_data)
    list = []
    items = soup.findAll('div', {'class':'item'})
    for theItem in items:
        newItem = Item()
        name = theItem.find('a',{'class':'nombre sin_subrayar'})
        if name:
            newItem.title=unicode(name.string)
            newItem.price=''#get_price(theItem)
            newItem.link="http://www.todocoleccion.net"+name['href']
            newItem.image=theItem.find('div',{'class':'foto'}).img['src']
            newItem.fromPage='TodoColeccion'
            list.append(newItem)
    return list

def get_price(item):
    price=item.find('p',{'class':'precio'})
    precio_directa = price.find('span',{'class':'precio_directa'})
    if precio_directa:
        logging.info("Precio" + unicode(precio_directa.string))
        logging.info("Precio" + unicode(price.span.span.string))
        logging.info("Precio" + unicode(price.span.string))
    return precio_directa
