import requests
from bs4 import BeautifulSoup
import os
import textwrap
import sys
import wikipedia


query = str(sys.argv[2])
site = str(sys.argv[1])
print("Want to know about the command : " + query)
print("Fetching information for the command "+query+" from "+site+".")
if(site == "wikipedia" or site == "wiki"):
	
    result = wikipedia.summary("'%s' linux command" %query, sentences = 7)
    print(result)
                      
# soup=BeautifulSoup(html_doc, 'html.parser')
# print(soup)
'''for p in soup.find_all('p'):
            # print textwrap.fill(p.get_text())
            # print textwrap.dedent(p.get_text()).strip()
            print textwrap.fill(textwrap.dedent(p.get_text()).strip(), initial_indent='', subsequent_indent='    ')

'''
