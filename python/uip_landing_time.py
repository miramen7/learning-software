# NIO_COMPONENT automation_test
from uip import *

def xpath_to_element_tens(driver, xpath, high_light):
    try:
        element = driver.find_element_by_xpath(xpath)

    except selenium.common.exceptions.NoSuchElementException:
        element = None

    if element is None:
        time.sleep(0.1)
        xpath_to_element_tens(driver, xpath, high_light)

    else:
        if high_light:
            highlight(element)

    return element

def main():
    args = process_argument()
    hostname_credential = get_hostname_credential(args.hostname_credential)
    customers = get_customers(args.customer, hostname_credential)
    var = raw_input('\nTest Landing reponse time?')
    if var != 'n':
        for host in hostname_credential:
            if host['customer'] in customers:
                display_text = '\ntesting customer %s at %s?' %(host['customer'], host['hostname'])
                var = raw_input(display_text)
                if var == 'n':
                    continue

                total_time = datetime.datetime.now() - datetime.datetime.now()
                command = 'ping %s -c 5' %(host['hostname'])
                subprocess.call(command, shell=True)
                loading_time = []
                login_url = 'https://%s.vpn.niometrics.com' %(host['hostname'])
                for i in range(5):
                    driver = webdriver.Chrome(args.chrome_driver_path)
                    driver.get(login_url)
                    element = name_to_element(driver, 'username')
                    element.send_keys(host['username'])
                    element = name_to_element(driver, 'password')
                    element.send_keys(host['password'])
                    time.sleep(.5)
                    element.submit()
                    start = datetime.datetime.now()
                    element = xpath_to_element_tens(driver, '//*[@id="show_more"]',False)
                    end = datetime.datetime.now()
                    delta = end - start
                    loading_time.append(delta)
                    total_time += delta
                    driver.quit()

                print loading_time
                print 'average %s' %(total_time / 5)


if __name__ == "__main__":
    main()
