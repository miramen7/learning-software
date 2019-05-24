#Automation test Login module
import argparse
import collections
import os
import json
import time
import datetime
import urllib2
import selenium as sel
from selenium import webdriver

def process_argument():
	parser = argparse.ArgumentParser(description = '')
	parser.add_argument('-customer','--customer', help = 'customer, comma separated for multiple values')
	parser.add_argument('-hostname_credential','--hostname_credential', default = 'hostname_credential.json', help = 'hostname credential file')
	parser.add_argument('-cdp','--chrome_driver_path', default = '/Applications/chromedriver', help = 'chrome driver path, default = "/Applications/chromedriver" ')
	args = parser.parse_args()
	return args

def get_hostname_credential(args_hostname_credential):
    if os.path.isfile('../' + args_hostname_credential):
        orig = os.path.dirname(os.path.realpath(__file__))
        os.chdir('../')
        hostname_credential = json.load(open(args_hostname_credential))
        os.chdir(orig)

    else:
        print 'file "../hostname_credential.json" not exist, exiting'
        quit()

    return hostname_credential

def get_customers(args_customer, hostname_credential):
    if args_customer is None:
        customers = []        
        for host in hostname_credential:
            customers.append(host['customer'])


    else:
        customers = args_customer.split(',')

    return customers

def name_to_element(driver, name):
    time.sleep(1)
    try:
        element = driver.find_element_by_name(name)

    except selenium.common.exceptions.NoSuchElementException:
        element = None

    if element is None:
        time.sleep(1)
        name_to_element(driver, name)

    time.sleep(1)
    return element

def xpath_to_element(driver, xpath, high_light):
    time.sleep(1)
    try:
        element = driver.find_element_by_xpath(xpath)

    except selenium.common.exceptions.NoSuchElementException:
        element = None

    if element is None:
        time.sleep(1)
        xpath_to_element(driver, xpath, highlight)

    else:
        if high_light:
            highlight(element)

    time.sleep(1)
    return element

def link_to_element(driver, link, high_light):
    time.sleep(1)
    try:
        element = driver.find_element_by_link_text(link)

    except selenium.common.exceptions.NoSuchElementException:
        element = None

    if element is None:
        time.sleep(1)
        link_to_element(driver, link, high_light)

    else:
        if high_light:
            highlight(element)

    time.sleep(1)
    return element

def main_uip():
	args = process_argument()
	hostname_credential = get_hostname_credential(args.hostname_credential)
	customers = get_customers(args.customer, hostname_credential)
	driver = webdriver.Chrome(args.chrome_driver_pat   h)
	print("Test login")
	for host in hostname_credential:
		if host['customer'] in customers:
			display_text = "\nLogin to %s at %s?" %(host['customer'],host['hostname'])
			var = raw_input(display_text)
			if var == 'n':
				continue

			conf_url = 'http://%s:8080/vo/conf/show?source=swaggerui' %host['hostname']
			response = urllib2.urlopen(conf_url)
			nio_conf = json.load(response)
			login_url = 'https://%s' %(host['hostname'])
			driver.get(login_url)
			element = name_to_element(driver, 'username')
			element.send_keys(host['username'])
			element = name_to_element(driver, 'password')
			element.send_keys(host['password'])
			time.sleep(.5)
			element.submit()

    driver.quit()
    print("done")

if __name__ == "__main__":
    main_uip()
