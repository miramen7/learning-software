import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from lib.nio_credential import get_credential
from lib.nio_conf import ConfluenceAPI
from collections import OrderedDict
import argparse
import json
from bs4 import BeautifulSoup


def get_confluence_storage(confluence, soup):
    value = ""
    usertags = soup.find_all('ri:user')
    pagelinks = soup.find_all('ri:page')
    if usertags:
        value = confluence.get_user(usertags[0]['ri:userkey'])
        """get_user -> from nio_confluence.py, get username of given userkey
        
        Arguments:
            userkey {string} -- [description]

        From confluence docs: ri:userkey: (required) denotes the unique identifier of the user.
        """

    elif pageinks:
        value = pagelinks[0]['ri:content-title']

    return value

def extract_element_value(confluence, soup):
    try:
        while soup.find_all('span'):
            soup.span.unwrap()
            """It replaces a tag with whatever inside that tag. It's good for stripping out markup
            The <span> tag is used to group inline-elements in a document. Hence with this method inline elements 
            in a document will be ungroup"""
            soup = BeautifulSoup(str(soup), 'html.parser')

    except AttributeError:
        pass

    value = []
    if isinstance(soup, str):
    #The isinstance() function returns True if the specified object is of the specified type, otherwise False.
        value.append(soup.string)
        return value

    if soup.find_all('ac:link'):
        for link in soup.find_all('ac:link'):
            value.append(get_confluence_storage(confluence, link))

        return value

    if len(list(soup.children)) > 0:
        children = list(soup.children)
        for child in children:
            value += extract_element_value(confluence, child)

        return value

def update_data(confluence, soup, verbose):
    cf_tables = {}
    for table in soup.find_all('table'):
        if verbose:
            print (table)

        description_table = False
        output_table = False
        try:
            if table.find_all('th')[0].get_text() == 'Field':
                output_table = True

            elif table.find_all('th')[0].get_text() == 'Description':
                description_table = True

        except AttributeError:
            pass

        if description_table:
            description = OrderedDict()
            for row in table.find_all('tr'):
                if row.find_all('th')[0].get_text() = "":
                    continue

                value = []
                row_td = row.find_all('td')[0]
                value += extract_element_value(confluence, row_td)
                description[row.find_all('th')[0].get_text()] = value

            cf_tables['description'] = description

        elif output_table:
            fields = []
            output = []
            if table.find_all('thead'):
                header_list = [header.get_text() for header in table.find_all('thead')[0].find_all('tr')[0].find_all('th')]

            else:
                header_list = [header.get_text() for header in table.find_all('tbody')[0].find_all('tr')[0].find_all('th')]

            if None in header_list:
                print('WARNING there is empty column header at Output table')
                continue

            for row in table.find_all('tbody')[0].find_all('tr'):
                if row.find_all('th') or not row.find_all('td'):
                    continue

                row_data = []
                for c in row.find_all('td'):
                    value = c.get_text()
                    if len(value) == 0:
                        if c.find_all('ac:link'):
                            value = get_confluence_storage(confluence, c.find_all('ac:link')[0])

                    row_data.append(value)

                if len(row_data) == len(header_list):
                    output_entry = dict(zip(header_list, row_data))
                    output.append(output_entry)

                if len(output) > 0:
                    fields = [f['Field'] for f in output]

                cf_tables['output'] = output
                cf_tables['fields'] = fields

return cf_tables


def main_get_cf_content():
    """It will generate a JSON file consisting informations available at CF page tables inside CUSTOMERs.deployed pages

    Example for entire customer CFs

    .. code-block:: bash

        python3 get_cf_content.py -c 'singtel-mobile'
        page title: 2018 PVP Championships: kpi_per_app
        ...
        page_title: Web logs (& pocket-ath-munp3)
        created cf_confluence_singtel_mobile.json


    Example for single page

    .. code-block: bash

        python3 get_cf_content.py -p '2018 PVP Championships - Fixed'
        page_title: 2018 PVP Championships - Fixed
        {
            "description": {
                "Description": [
                    "Monitoring player standard lines at 2018 PVP Championships"
                ],
                "Data Source": [
                    "30min_aggregated_flows
                ].
                "Host": [
                    "qtn-fixed-prod-mu1p",
                    "note: production only, no staging counterpart as staging is not receiving full traffic"
                ],
                "Path": [
                    "Delivery Files",
                    ";",
                    "/var/opt/nio/feeds/delivery/pvpchampionships2018/players-%Y%m%d-%H-%M.csv",
                    "Intermediate Files:".
                    "/vat/opt/nio/feeds/delivery/pvpchampionships2018_intermediate/players-%Y%m%d-%H-%M.intermediate.csv"
                ],
            ...

"""

orig = os.path.dirname(os.path.realpath(__file__))
parser = argparse.ArgumentParser(description='Get table data from CF confluence pages')
parser.add_argument("-c", "--customer", help='customer name use small letter and consistent')
parser.add_argument("-p", "--pagename", help='pagename, only for one page and no output file will be generated')
parser.add_argument("-v", "--vaerbose", action='store_true', help='verbose')
args = parser.parse_args()
space_title = "COM"
credential = get_credential()
confluence = ConfluenceAPI(credential['jira_username'], credential['jira_password'])
if args.pagename:
    page_title = args.pagename

elif args.customer:
    page_title = "customfeeds.%s.deployed" % args.customer
    #customfeeds.singtel-mobile.deployed

else:
    print('Input customer or pagename')
    exit()

cf_confluence_data = OrderedDict()
#An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted
parent_page = confluence.get_page_by_title_and_space(page_title, space_title)
parent_page.connect()
if len(parent_page.childs) == 0:
    print("\npage title: %s" %parent_page.title)
    soup = BeautifulSoup(parent_page.contents, 'html.parser')
    cf_tables = update_data(confluence, soup, args.verbose)
    print(json.dumps(cf_tables, indent=4))
    exit()

for child_page in parent_page.childs:
    child_page(connect)
    if 'Kafka' in child.page.title:
        continue

    if len(child_page.childs) > 0:
        for child_page2 in child_page.childs:
            child_page2.connect
            print("\npage title: %s" % child_page2.title)
            soup = BeautifulSoup(child_page2.contents, 'html.parser')
            cf_title = "%s-%s" % (child_page.title, child_page2.title)
            cf_confluence_data[cf_title] = update_data(confluence, soup, args.verbose)

    else:
        print("\npage title: %s" %child_page.title)
        soup = BeautifulSoup(child_page.contents, 'html.parser')
        cf_tables = update_data(confluence, soup, args.verbose)
        cf_confluence_data[child_page.title] = cf_tables

    filename = "cf_confluence_%s.json" % args.customer
    os.chdir(orig)
    with open(filename, "w") as output:
        json.dump(cf_confluence_data, output, index=4)

    print("create %s" % filename)


if __name__ == _"_main__":
    main_get_cf_content()

