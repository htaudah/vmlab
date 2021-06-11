#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule
# pylint: disable=no-name-in-module
from ansible.module_utils.ansibleutils import (
    create_results,
    return_results
)

DOCUMENTATION = '''
---
module: airwatch_db_upgradepath
filename: airwatch_db_upgradepath.py
author: Robert Rounsaville  rrounsaville@vmware.com
created: 04/9/2018 - Initial creation
short_description: |
    Takes a list of major airwatch versions and
    returns all versions needed for a multi-step database upgrade.
notes: does not support Check mode, it breaks it!
description: |
    Accepts the current and target airwatch version
    and a file containing a list of available versions
    returns a list of versions require for a database upgrade (db_upgrade_path)
requirements:
    - must be run as a local action on the Ansible server as python is not present
      on target windows nodes
options:
    - currentversion is required, in the octal dot notation, IE; 8.4.1.0 for AirWatch 8.4 FP1
    - targetversion is required, in the octal dot notation, IE; 8.4.1.0 for AirWatch 8.4 FP1
    - versionfile is path to a local versions list
command_line:
    - ansible -m airwatch_db_upgradepath -i /opt/aw-emm-automation-ansible/inventory/default_localhost localhost -a "currentversion='8.4.0.400' targetversion='9.6.0.0' versionfile='/var/lib/jenkins/jobs/lists/AWVersions'"
'''

from selenium import webdriver

# uem_url = ("https://uemc.haramco.org/AirWatch")
# browser.get(url)
# browser.find_element_by_id('UserName').send_keys('Administrator')
# browser.find_element_by_id('UserName').submit()
# browser.find_element_by_id('Password').send_keys('Baltona31@')
# browser.find_element_by_id('Password').submit()

# browser.find_element_by_css_selector('a.js-close-welcome-modal').click()
# browser.find_element_by_css_selector('a[aria-label="Global Organization Group Drop Down Menu"]').click()
# browser.find_element_by_css_selector('a[data-name=Haramco]').click()
# browser.find_element_by_css_selector('a[href="#/AirWatch/Menu/ConfigAndSettings/Groups"]').click()
# browser.find_element_by_css_selector('a[aria-label="All Settings Opens Dialog"]').click()
# browser.find_elements_by_css_selector('a[href="/AirWatch/Settings/CategoryLanding/7"]')[1].click()
# browser.find_elements_by_css_selector('a[href="/AirWatch/Settings/DeviceRootCertificate"]')[1].click()
# browser.find_element_by_css_selector('input[name="GenerateNewCertificate"]').submit()
# browser.find_element_by_css_selector('a[aria-label="Close Dialog"]').click()

# browser.find_element_by_css_selector('a[aria-label="All Settings Opens Dialog"]').click()
# browser.find_elements_by_css_selector('a[href="/AirWatch/Settings/CategoryLanding/86"]')[1].click()
# browser.find_elements_by_css_selector('a[href="/AirWatch/ContentGateway"]')[1].click()
# browser.find_element_by_css_selector('label[for="ContentGatewayEnabled_True"]').click()
# browser.find_element_by_css_selector('input[name="Save"]').click()

def main():
    module = AnsibleModule(
        argument_spec = dict(
            ssh_password = dict(type='str', required=True),
            root_password = dict(type='str', required=True),
            admin_password = dict(type='str', required=True),
            database_path = dict(type='str', required=True),
            database_user = dict(type='str', required=True),
            database_password = dict(type='str', required=True),
            timeout = dict(type='int', default=20),
        ),
        supports_check_mode = False
    )

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome('/usr/local/share/chromedriver', options=chrome_options)
    browser.implicitly_wait(10)

    access_url = ("https://access01.haramco.org/cfg/setup")
    browser.get(access_url)
    browser.find_element_by_id('pass').send_keys('Baltona31@')
    browser.find_element_by_id('passConf').send_keys('Baltona31@')
    browser.find_element_by_id('rootPass').send_keys('Baltona31@Baltona31@')
    browser.find_element_by_id('rootPassConf').send_keys('Baltona31@Baltona31@')
    browser.find_element_by_id('sshPass').send_keys('Baltona31@Baltona31@')
    browser.find_element_by_id('sshPassConf').send_keys('Baltona31@Baltona31@')
    browser.find_element_by_id('nextButton').click()

    time.sleep(10)

    browser.find_element_by_css_selector('input.externDB').click()
    browser.find_element_by_id('jdbcurl').send_keys('jdbc:sqlserver://MainAG.haramco.org:1433;DatabaseName=accessdb')
    browser.find_element_by_id('dbUsername').send_keys('temp_acct')
    browser.find_element_by_id('dbPassword').send_keys('Baltona31@')
    browser.find_element_by_id('nextButton').click()

    # Now wait up to 20 minutes for initialization to complete
    count = 0
    while browser.current_url != success_url:
        time.sleep(60)
        count += 1
        if count == timeout:
            module.fail_json(msg="Timed out while waiting for initializationt to complete")

    browser.quit()


if __name__ == '__main__':
    main()
