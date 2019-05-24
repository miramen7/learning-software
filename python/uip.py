# NIO_COMPONENT automation_test
import argparse
import collections
import os
import json
import time
import datetime
import subprocess
import urllib2
import selenium
from selenium import webdriver

def process_argument():
    parser = argparse.ArgumentParser(description = '')
    parser.add_argument('-customer', '--customer', help = 'customers, comma separated for multiple values')
    parser.add_argument("-hostname_credential", '--hostname_credential', default='hostname_credential.json', help='hostname credential file')
    parser.add_argument("-cdp", '--chrome_driver_path', default='/Applications/chromedriver', help='chrome driver path, default="/Applications/chromedriver" ')
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

def highlight(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
            element, s
        )
    original_style = element.get_attribute('style')
    for i in range(3):
        apply_style("background: red;")
        time.sleep(.3)
        apply_style(original_style)
        time.sleep(.3)


def get_setting_suffix(nio_conf):
    setting_suffix = collections.OrderedDict()
    setting_suffix['nio_api'] = nio_conf['api']['endpoints'],
    setting_suffix['advanced/modules'] = nio_conf['nioweb']['modules'],
    setting_suffix['ldap'] = nio_conf['auth']['ldap'],
    setting_suffix['appliance/email_server'] = nio_conf['smtp'],
    setting_suffix['management/web_ui_access'] = "",
    setting_suffix['appliance/branding'] = [
        nio_conf['nio']['reports']['parameters']['company_name'],
        nio_conf['nio']['site_disclaimer'],
        nio_conf['nioweb']['landing_welcome_message'],
        nio_conf['nioweb']['landing_sub_welcome_message']
    ],
    setting_suffix['advanced/feeds'] = nio_conf['nioweb']['feeds']['availability'],
    setting_suffix['appliance/time'] = nio_conf['time'],
    setting_suffix['ui/kb'] = "",
    #
    setting_suffix['advanced/dashboards'] = [
        nio_conf['nioweb']['panels']['dashboard'],
        nio_conf['nioweb']['panels']['beta_page'],
        nio_conf['nioweb']['dashboard_settings']['network']['scopes'],
        nio_conf['nioweb']['dashboard_settings']['business']['scopes']
    ],
    setting_suffix['advanced/panels'] = [
        nio_conf['nioweb']['panels']['dashboard'],
        nio_conf['nioweb']['dashboard_settings']['subscriber']['panels'],
    ],
    setting_suffix['ui/network_tabs'] = nio_conf['nioweb']['network_tabs'],
    setting_suffix['advanced/rating'] = nio_conf['rating'],
    setting_suffix['ui/network'] = [
        nio_conf['nioweb']['panel_config']['network'],
        nio_conf['nioweb']['ia_mapping']
    ],
    #
    setting_suffix['appliance/regional_info'] = [
        nio_conf['nio']['reports']['parameters']['region'],
        nio_conf['nio']['reports']['parameters']['local_domain_suffix'],
        nio_conf['nio']['reports']['parameters']['competitors_domains']
    ],
    setting_suffix['advanced/explorer'] = nio_conf['nioweb']['modules']['Explorer']['customization'],
    setting_suffix['advanced/reports'] = [
        nio_conf['nio']['reports']['generation_statistics']['time'],
        nio_conf['nio']['reports']['mail_links']
    ],
    #
    setting_suffix['servers/machine'] = nio_conf['nio']['machines'],
    #
    setting_suffix['advanced/networks_specs'] = "",
    setting_suffix['servers/internal_external_network'] = [
        nio_conf['nio']['internal_networks'],
        nio_conf['nio']['external_networks'],
        nio_conf['nio']['mobile_network_type'] 
    ],
    setting_suffix['ui/network_partners'] = "",
    setting_suffix['advanced/subscriber_segment'] = nio_conf['segments'],
    setting_suffix['management/ip_groups'] = "",
    #
    setting_suffix['advanced/interface'] = nio_conf['nio']['ignore_dup_pkts'],
    setting_suffix['networks/proxy_peeling'] = nio_conf['nio']['proxy_peel'],
    #
    setting_suffix['appliance/software_updates'] = nio_conf['updates'],
    setting_suffix['appliance/site_license'] = [
        nio_conf['nio']['site_key'],
        nio_conf['nio']['site_desc'],
        nio_conf['nio']['site_disclaimer'] 
    ],
    setting_suffix['ui/rpm_versions'] = "",
    #
    setting_suffix['log/remote_syslog'] = nio_conf['nio']['log']['syslog'],
    setting_suffix['management/ssh_access'] = nio_conf['ssh'],
    setting_suffix['servers/proxy_server'] = nio_conf['proxy'],
    setting_suffix['log/log_retention'] = nio_conf['nio']['log']['retain_days']
    return setting_suffix

def get_permission_list():
    permission_list = []
    for i in range(18):
        if i != 1:
            text = '//*[@id="heading%s"]/h4' %(str(i))
            permission_list.append(text)


    return permission_list

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
    driver = webdriver.Chrome(args.chrome_driver_path)
    print 'This script to test UI Platform'
    print 'Based on feature check list on https://confluence.niometrics.com/display/COM/UI-Platform'
    for host in hostname_credential:
        if host['customer'] in customers:
            display_text = '\ntesting customer %s at %s?' %(host['customer'], host['hostname'])
            var = raw_input(display_text)
            if var == 'n':
                continue

            conf_url = 'http://%s:8080/v0/conf/show?source=swaggerui' %(host['hostname'])
            response = urllib2.urlopen(conf_url)
            nio_conf = json.load(response)
            setting_suffix = get_setting_suffix(nio_conf)
            login_url = 'https://%s.vpn.niometrics.com' %(host['hostname'])
            var = raw_input('\nloading the login page?')
            if var == 'n':
                continue

            driver.get(login_url)
            var = raw_input('\nlogin with username = admin and password = dummy?')
            if var != 'n':
                element = name_to_element(driver, 'username')
                element.send_keys('admin')
                element = name_to_element(driver, 'password')
                element.send_keys('dummy')
                time.sleep(.5)
                element.submit()
                text = '\nclick and hover the mouse to password box, expected:\n"Incorrect username or password"'
                var = raw_input(text)

            text = '\nlogin with user which do not have any permission?'
            var = raw_input(text)
            if var != 'n':    
                driver.get(login_url)
                element = name_to_element(driver, 'username')
                element.send_keys('nio-test-no-permission')
                element = name_to_element(driver, 'password')
                element.send_keys('nio-test-no-permission')
                time.sleep(.5)
                element.submit()
                text = '\nclick and hover the mouse to password box, expected:\n"You do not have any role assigned"'
                var = raw_input(text)

            text = '\nlogin with admin credential?'
            var = raw_input(text)
            if var == 'n':
                continue

            driver.get(login_url)
            element = name_to_element(driver, 'username')
            element.send_keys(host['username'])
            element = name_to_element(driver, 'password')
            element.send_keys(host['password'])
            time.sleep(.5)
            element.submit()
            var = raw_input('\ncheck customer logo?')
            branding_url = '%s/settings?referrer=landing#/engine_config/appliance/branding' %(login_url)
            if var != 'n':
                element = xpath_to_element(driver, '//*[@id="container"]/div[1]/div[2]/img', True)
                driver.get(branding_url)
                element = xpath_to_element(driver, '//*[@id="config-content"]/div[1]/form/fieldset/div[1]/img[2]', True)
            
            var = raw_input('\ncheck Niometrics logo?')
            if var != 'n':
                driver.get(login_url)
                element = xpath_to_element(driver, '//*[@id="container"]/div[1]/div[1]/img', True)
            
            var = raw_input('\ncheck landing welcome message?')
            if var != 'n':
                conf_value = nio_conf['nioweb']['landing_welcome_message']
                print 'expected :\n"%s"' % (conf_value)
                element = xpath_to_element(driver, '//*[@id="container"]/div[3]/div[1]/div/div[1]', True)
                driver.get(branding_url)
                element = xpath_to_element(driver, '//*[@id="site-disclaimer2"]', True)
            
            var = raw_input('\ncheck last login time?')
            if var != 'n':
                driver.get(login_url)
                element = xpath_to_element(driver, '//*[@id="container"]/div[3]/div[2]/div[2]/ul[1]/li[2]/span',True)
            
            var = raw_input('\ncheck recently accessed module?')
            if var != 'n':
                driver.get(login_url)
                element = xpath_to_element(driver, '//*[@id="container"]/div[3]/div[2]/div[2]/ul[1]/li[4]',True)
                element = xpath_to_element(driver, '//*[@id="show_more"]',True)
                element.click()
                element = xpath_to_element(driver, '//*[@id="container"]/div[3]/div[2]/div[2]/ul[1]/li[4]',True)
            
            var = raw_input('\ncheck module shortcuts?')
            if var != 'n':
                text = 'please manually verify that module shortcust listed there are correct\n'
                text += 'and each link direct to correct module'
                var = raw_input(text)
            
            var = raw_input('\ncheck System Setting?')
            if var != 'n':
                setting_url = login_url + '/settings#/engine_config/'
                for suffix in setting_suffix:
                    setting_sub_url = setting_url + suffix
                    driver.get(setting_sub_url)
                    if setting_suffix[suffix] != "":
                        print suffix
                        print json.dumps(setting_suffix[suffix], indent=4)

                    var = raw_input('\nnext?')
            

            var = raw_input('\ncheck Change Setting and Automatic nio-web Restart?')
            if var != 'n':
                driver.get(branding_url)
                time.sleep(1)
                current_disclaimer = nio_conf['nio']['site_disclaimer']
                test_disclaimer = 'Test Change Site Disclaimer'
                element = xpath_to_element(driver, '//*[@id="site-disclaimer"]',True)
                var = raw_input('\nchange Site Disclaimer with "Test Change Site Disclaimer"?')
                element.clear()
                time.sleep(.5)
                element.send_keys(test_disclaimer)
                time.sleep(.5)
                var = raw_input('\napply changes?')
                if var != 'n':
                    element = xpath_to_element(driver, '//*[@id="config-actions"]/button[1]',False)
                    element.click()
                    print 'wait two minutes'
                    time.sleep(120)
                    var = raw_input('\nCheck nio-web active time?')
                    command = 'ssh %s "/usr/sbin/service nio-web status | grep Active"' % (host['hostname'])
                    subprocess.call(command, shell=True)
                    var = raw_input('\nContinue see applied disclaimer?')
                    driver.get(login_url)
                    element = link_to_element(driver, 'Sign Out', False)
                    element.click()
                    print '\nexpected:\n%s' %(test_disclaimer)
                    element = xpath_to_element(driver, '//*[@id="main"]/div[2]',True)
                    var = raw_input('\nrevert the previous disclaimer"?')
                    driver.get(login_url)
                    element = name_to_element(driver, 'username')
                    element.send_keys(host['username'])
                    element = name_to_element(driver, 'password')
                    element.send_keys(host['password'])
                    time.sleep(.5)
                    element.submit()
                    time.sleep(.5)
                    driver.get(branding_url)
                    element = xpath_to_element(driver, '//*[@id="site-disclaimer"]',False)
                    element.clear()
                    time.sleep(.5)
                    element.send_keys(current_disclaimer)
                    var = raw_input('\napply changes?')
                    element = xpath_to_element(driver, '//*[@id="config-actions"]/button[1]',False)
                    element.click()
                    print 'wait two minutes'
                    time.sleep(120)
            

            var = raw_input('\ncheck user permission?')
            if var != 'n':
                permission_url = login_url + '/user/app/pems'
                driver.get(permission_url) 
                permission_list = get_permission_list()
                var = raw_input('\nnext?')
                for permission in permission_list:
                    
                    element = xpath_to_element(driver, permission,True)
                    try:
                        element.click()

                    except selenium.common.exceptions.WebDriverException:
                        continue

                    var = raw_input('\nnext?')
                    try:
                        element.click()

                    except selenium.common.exceptions.WebDriverException:
                        continue



            var = raw_input('\ncheck user roles?')
            if var != 'n':
                roles_url = login_url + '/user/app/roles'
                driver.get(roles_url) 

            var = raw_input('\nlogout?')
            driver.get(login_url)
            element = link_to_element(driver, 'Sign Out', True)
            element.click()
            time.sleep(1)
        

    driver.quit()
    print 'done'

if __name__ == "__main__":
    main_uip()



