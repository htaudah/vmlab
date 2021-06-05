#!/usr/bin/python3
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('/usr/local/share/chromedriver', options=chrome_options)
browser.implicitly_wait(10)
uem_url = ("https://uemc.haramco.org/AirWatch")
access_url = ("https://uemc.haramco.org/AirWatch")
browser.get(url)
browser.find_element_by_id('UserName').send_keys('Administrator')
browser.find_element_by_id('UserName').submit()
browser.find_element_by_id('Password').send_keys('Baltona31@')
browser.find_element_by_id('Password').submit()

browser.find_element_by_css_selector('a.js-close-welcome-modal').click()
browser.find_element_by_css_selector('a[aria-label="Global Organization Group Drop Down Menu"]').click()
browser.find_element_by_css_selector('a[data-name=Haramco]').click()
browser.find_element_by_css_selector('a[href="#/AirWatch/Menu/ConfigAndSettings/Groups"]').click()
browser.find_element_by_css_selector('a[aria-label="All Settings Opens Dialog"]').click()
browser.find_elements_by_css_selector('a[href="/AirWatch/Settings/CategoryLanding/7"]')[1].click()
browser.find_elements_by_css_selector('a[href="/AirWatch/Settings/DeviceRootCertificate"]')[1].click()
browser.find_element_by_css_selector('input[name="GenerateNewCertificate"]').submit()
browser.find_element_by_css_selector('a[aria-label="Close Dialog"]').click()

browser.find_element_by_css_selector('a[aria-label="All Settings Opens Dialog"]').click()
browser.find_elements_by_css_selector('a[href="/AirWatch/Settings/CategoryLanding/86"]')[1].click()
browser.find_elements_by_css_selector('a[href="/AirWatch/ContentGateway"]')[1].click()
browser.find_element_by_css_selector('label[for="ContentGatewayEnabled_True"]').click()
browser.find_element_by_css_selector('input[name="Save"]').click()

# WS1 Access
browser.find_element_by_id('pass').send_keys('Baltona31@')
browser.find_element_by_id('passConf').send_keys('Baltona31@')
browser.find_element_by_id('rootPass').send_keys('Baltona31@Baltona31@')
browser.find_element_by_id('rootPassConf').send_keys('Baltona31@Baltona31@')
browser.find_element_by_id('sshPass').send_keys('Baltona31@Baltona31@')
browser.find_element_by_id('sshPassConf').send_keys('Baltona31@Baltona31@')
browser.find_element_by_id('nextButton').click()

browser.find_element_by_css_selector('input.externDB').click()
browser.find_element_by_id('jdbcurl').send_keys('jdbc:sqlserver://MainAG:1433;DatabaseName=accessdb')
browser.find_element_by_id('dbUsername').send_keys('temp_acct')
browser.find_element_by_id('dbPassword').send_keys('Baltona31@')
browser.find_element_by_id('nextButton').click()

html_source = browser.page_source
browser.quit()
