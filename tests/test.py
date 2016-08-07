#!/usr/bin/env python
"""
test of selenium
"""
from selenium.webdriver.common.keys import Keys
#
from gdrivepublic import browser

drv = browser()

drv.get('http://www.python.org')
assert 'Python' in drv.title
el = drv.find_element_by_name("q")
el.clear()
el.send_keys('pycon')
el.send_keys(Keys.RETURN)
assert 'No results found.' not in drv.page_source
drv.close()