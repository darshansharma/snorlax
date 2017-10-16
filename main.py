import requests
from bs4 import BeautifulSoup
import os
import textwrap

query=os.environ['snorlax']
print "fetching information "+query
r=requests.get("https://en.wikipedia.org/wiki/%s"%query)
html_doc=r.text
soup=BeautifulSoup(html_doc, 'html.parser')
for p in soup.find_all('p'):
	#print textwrap.fill(p.get_text())
        #print textwrap.dedent(p.get_text()).strip()
        print textwrap.fill(textwrap.dedent(p.get_text()).strip(), initial_indent='', subsequent_indent='    ')
