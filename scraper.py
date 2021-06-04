#!/usr/bin/python3
from bs4 import BeautifulSoup
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('/usr/local/share/chromedriver', options=chrome_options)
url = ("https://uemc.haramco.org/AirWatch")
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

html_source = browser.page_source
soup = BeautifulSoup(html_source, 'lxml')
browser.quit()

#token = soup.find('input', {'name': '__RequestVerificationToken'}).get('value')
