# NIO_COMPONENT automation_test
from uip import *

customer='telkomsel'
hostname='10.2.184.40'
username='admin'
password='niometrics'
login_url = 'https://%s' %(hostname)

def main_uip_session():
    args = process_argument()
    var = raw_input('\nverify your connection to telkomsel VPN\nContinue?')
    var = raw_input('\nStart with testing user session expire?')
    if var != 'n':
        driver1 = webdriver.Chrome(args.chrome_driver_path)
        driver1.get(login_url)
        element = name_to_element(driver1, 'username')
        element.send_keys('nio_test_expire')
        element = name_to_element(driver1, 'password')
        element.send_keys('niometrics')
        time.sleep(.5)
        element.submit()
        print '\nwait, session should be expired after 1 minute'
        time.sleep(60)
        var = raw_input('\ncheck sesion expire or not\ncontinue with non expire one?')
        driver1.get(login_url)
        element = name_to_element(driver1, 'username')
        element.send_keys('nio_test_multi_session')
        element = name_to_element(driver1, 'password')
        element.send_keys('niometrics')
        time.sleep(.5)
        element.submit()
        print '\nwait, session not should be expired after 1 minute'
        time.sleep(60)
        var = raw_input('\ncheck sesion expire or not\ncontinue with testing multiple session for allowed user?')
        driver2 = webdriver.Chrome(args.chrome_driver_path)
        driver2.get(login_url)
        element = name_to_element(driver2, 'username')
        element.send_keys('nio_test_multi_session')
        element = name_to_element(driver2, 'password')
        element.send_keys('niometrics')
        time.sleep(.5)
        element.submit()
        var = raw_input('\nboth login expected to be success')
        driver1.quit()
        driver2.quit()

    var = raw_input('\ncontinue testing multiple session login for unallowed user?')
    if var != 'n':
        driver3 = webdriver.Chrome(args.chrome_driver_path)
        driver3.get(login_url)
        element = name_to_element(driver3, 'username')
        element.send_keys('nio_test_one_session')
        element = name_to_element(driver3, 'password')
        element.send_keys('niometrics')
        time.sleep(.5)
        element.submit()
        driver4 = webdriver.Chrome(args.chrome_driver_path)
        driver4.get(login_url)
        element = name_to_element(driver4, 'username')
        element.send_keys('nio_test_one_session')
        element = name_to_element(driver4, 'password')
        element.send_keys('niometrics')
        time.sleep(.5)
        element.submit()
        var = raw_input('login at one of window expected to fail, click and hover the password box to check the warning\nlog_out?')
        driver3.get(login_url)
        element = link_to_element(driver3, 'Sign Out', False)
        element.click()
        element = name_to_element(driver3, 'username')

if __name__ == "__main__":
    main_uip_session()
