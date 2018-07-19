import zipfile

from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time

class DriverQA(object):
	
	def __init__(self):
		self.URL = ""

	def configDriver(self, browserWeb):
		if browserWeb == "firefox":
			firefox_capabilities = DesiredCapabilities.FIREFOX
			firefox_capabilities['marionette'] = True
			browser = webdriver.Firefox(capabilities=firefox_capabilities)
		else:
			co = Options()
			co.add_argument("--web-security=false")
			co.add_argument("--ssl-protocol=any")
			co.add_argument("--ignore-ssl-errors=true")
			co.add_argument('--log-level=3')
			browser = webdriver.Chrome(chrome_options=co)

		self.driver = browser

	def get_driver(self):
		return self.driver

	def get(self, value):
		self.driver.get(value)

	def find_element(self, value, *args):
		arg = args[0]
		if (len(arg) == 0):
			self.element = self.driver.find_element_by_id(value)
		elif (str(arg[0]) == 'name'): 
			self.element = self.driver.find_element_by_name(value)
		elif (str(arg[0]) == 'xpath'): 
			self.element = self.driver.find_element_by_xpath(value)
		elif (str(arg[0]) == 'css'): 
			self.element = self.driver.find_element_by_css_selector(value)
		elif (str(arg[0]) == 'link'): 
			self.element = self.driver.find_element_by_link(value)
		else: 
			self.element = self.driver.find_element_by_id(value)

	def send_keys(self, identify, value, *args):
		self.find_element(identify, args)
		self.element.send_keys(value)

	def click(self, identify, *args):
		self.find_element(identify, args)
		self.element.click()

	def get_text(self, identify, *args):
		self.find_element(identify, args)
		return self.element.text	

	def quit(self):
		self.driver.quit()

	def implicitly_wait(self, seconds):
		time.sleep(seconds)

	def page_source(self):
		return self.driver.page_source
