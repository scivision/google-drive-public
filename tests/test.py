#!/usr/bin/env python
"""
test of selenium
"""
from platform import system
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

syst = system().lower()

try:
    drv = webdriver.Firefox()
except Exception:
    if 'windows' in syst:
        chrome = 'c:\chromedriver\chromedriver.exe'
    elif 'linux' in syst:
        chrome = '/usr/lib/chromium-browser/chromedriver'
    else:
        chrome = None

    drv = webdriver.Chrome(chrome)

drv.get('http://www.python.org')
assert 'Python' in drv.title
el = drv.find_element_by_name("q")
el.clear()
el.send_keys('pycon')
el.send_keys(Keys.RETURN)
assert 'No results found.' not in drv.page_source
drv.close()