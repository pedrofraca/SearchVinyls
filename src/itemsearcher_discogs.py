import httplib
from pydoc import deque
import urllib

import BeautifulSoup
from BeautifulSoup import BeautifulSoup
from item import Item

          # For processing HTML


# To change this template, choose Tools | Templates
# http://www.discogs.com/sell/list?format=Vinyl&st=&q=los+planetas

__author__="pfraca"
__date__ ="$Jun 2, 2011 2:17:20 PM$"

def create_headers():
    headers = {}
    #headers['Content-Type'] = 'application/x-www-form-urlencoded'
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
        titleSpan = cols[1].find('span',{'class':'br_item_title'})
        if titleSpan:
            #image = cols[0].find('img')
            #newItem.image = image
            newItem.tittle = titleSpan.a.string
            newItem.fromPage="Discogs"
            priceSpan = cols[4].find('span',{'class':'price'})
            if priceSpan:
                newItem.price=priceSpan.string
            list.append(newItem)

    return list

