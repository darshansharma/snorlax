import requests
import argparse
from bs4 import BeautifulSoup
import os
import textwrap
import sys
import wikipedia

sources = ['wikipedia', 'wiki', 'google', 'stackoverflow']

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--site", default="wikipedia", choices=sources)
parser.add_argument("-q", "--query", default="", required=True, help="command to search")

args = parser.parse_args()
print("Want to know about the command : " + args.query)
print("Fetching information for the command "+args.query+" from "+args.site+".")
if(args.site == "wikipedia" or args.site == "wiki"):
	
    result = wikipedia.summary("'%s' linux command" %args.query, sentences = 7)
    print(result)
                      
# soup=BeautifulSoup(html_doc, 'html.parser')
# print(soup)
'''for p in soup.find_all('p'):
            # print textwrap.fill(p.get_text())
            # print textwrap.dedent(p.get_text()).strip()
            print textwrap.fill(textwrap.dedent(p.get_text()).strip(), initial_indent='', subsequent_indent='    ')

'''
