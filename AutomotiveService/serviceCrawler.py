__author__ = 'BharatRaju'


import urllib
import HTMLParser
import re
from bs4 import BeautifulSoup
#from urllib.parse import urljoin
from urlparse import urlparse
from urlparse import urlsplit
from urlparse import urljoin
import urlparse
import time
import threading
import operator
import sys
from urllib2 import urlopen
import robotparser


#given:
#returns:
#description:
#example:
def canonicalization(url,root):
    if url:
        url_1 = urlparse.urlparse(url)

        #url starting with '/' needs to be added to the root
        if url[0]!='h':
            url = urljoin(root,url)
        #removing default port

        try:
            if url_1.port:
                url = (url_1.geturl()).replace(':' + str(url_1.port), '')
        except:
            url=url

        #removing '#' and everything after it
        url = url.split('#')[0]

        #removing . and .. and removing '//'
        url_split=url.split('//')
        if len(url_split)>1:
            #url_split[1] = url_split[1].replace('/.+','')
            #url_split[1] = re.sub('/.+/','/',url_split[1]).strip()#url_split[1].replace('/.+','')
            url_split[1] = re.sub( '/+', '/', url_split[1]).strip()
            url = url_split[0] + '//' + url_split[1]

        url=url.replace('\r','')

        #remove the fragments
        #url = urlparse.urldefrag(url)[0]

        #forcing trailing /
        #if len(url)>1:
        #    if url[-1] != '/':
        #        url = url+'/'

        return(url)
    else:
        return(url)



#Given:
#returns:
#description:
#example:
def crawling_initial_seeds(frontier,frontier_file):
    #initialize each link as (link and number of incoming links to the node)
    #frontier = set(frontier)

    incoming_links={}
    iterated=set([])
    for seed in seeds:
        if seed not in iterated:
            iterated.add(seed)
        try:
            handle = urllib.urlopen(seed)
            http_headers = handle.info()
            http_header = str(http_headers)
        except:
            frontier = frontier-set([url])
            continue
        text =  handle.read()
        soup = BeautifulSoup(text)
        raw_html = str(soup)
        frontier_file.write('url_here:' +str(seed)+ '\n')
        frontier_file.write('header:' + http_header+'\n')
                #frontier_file.write('page contents:' + '\n')
        frontier_file.write('raw_html:' + raw_html+ '\n')
        frontier_file.write('urls_out:' + '\n')

        frontier_seeds = set([])
        frontier_iteration=set([])
        for link in soup.find_all('a'):
            if 'href' in link.attrs:
                url = canonicalization(link.attrs['href'],seed)
                if 'offer' in url or 'coupon' in url:
                    if url:
                        frontier_seeds.add(url)
                        if url in incoming_links:
                            incoming_links[url]=incoming_links[url]+1
                        else:
                            incoming_links[url]=1
                    else:
                        continue

        frontier_iteration = frontier_iteration.union(frontier_seeds)
        i=1
        #Commented because reading the existing file
        for each_item in frontier_seeds:
            try:
                frontier_file.write(str(i) + ':' + each_item + '\n')
            except:
                continue
            i=i+1

        frontier = set(frontier).union(frontier_iteration)
        frontier=frontier-iterated
    return frontier,iterated,incoming_links


frontier_file = file("frontier_new.txt","wb")
frontier = set([])#set(['http://www.epa.gov/radiation/rert/tmi.html'])
iterated = set([])
domains = set([])
incoming_links = {}#{'http://www.epa.gov/radiation/rert/tmi.html':1}
i=0

#crawling initial seed first
seeds = set(['http://www.firestonecompleteautocare.com/offers/'])

frontier,iterated,incoming_links = crawling_initial_seeds(seeds,frontier_file)