import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
#from lib.nio_credential import get_credential
#from lib.nio_conf import ConfluenceAPI
from collections import OrderedDict
import argparse
import json
import requests
from bs4 import BeautifulSoup




# Create a variable with the url
url = 'https://translate.google.com/#view=home&op=translate&sl=auto&tl=en&text=santai'
r = requests.get(url)

# Get the text of the contents
html_content = r.text

# Convert the html content into a beautiful soup object
soup = BeautifulSoup(html_content, 'lxml')
#print(soup.title)


# View the title tag of the soup object



#print(soup.find_all('div', attrs={'class': 'page tlid-homepage homepage translate-text'}))

try:
    while soup.find_all('span'):
        soup.span.unwrap()
        """It replaces a tag with whatever inside that tag. It's good for stripping out markup
        The <span> tag is used to group inline-elements in a document. Hence with this method inline elements 
        in a document will be ungroup"""
        soup = BeautifulSoup(str(soup), 'html.parser')

except AttributeError:
    pass


print(soup.find_all('span', {'lang': 'en'}))


for a in soup.find_all('div', {'class': 'result-shield-container tlid-copy-target'}):
    print a
    print a.get_text()

"""for b in soup.find_all('div', attrs={'class': 'frame'}):
    for c in b_descendants:
        print c.text
        print b.text
        for d in c.find_all('div'):
            print d
            for e in d.find_all('div'):
                for f in e.find_all('div'):
                    for g in f.find_all('div'):
                        print g
                        for h in g.find_all('div'):
                            #print h
                            for i in h.find_all('div'):
                                for j in i.find_all('div'):
                                    for k in j.find_all('div'):
                                        for l in k.find_all('div'):
                                            print l
                                            test = l.find_all("div", {"class": "test_dummy"})
                                            print(test)
                                            print(test.get_text())"""

"""print(soup.find_all('textarea'))
for a in soup.find_all('textarea'):
    print a
    if a.find_all('div')[0].get_text() == 'textarea':
        print a.get_text()



                                                #   headline = entry.find(class_='headline')
                                                #   if headline is not None:
                                                #       title = headline.get_text()

#print(soup.find("div", {"class=tlid-translation translation"}))#.get_text(strip=True)"""