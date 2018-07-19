class Login:
	def __init__(self, driverQA):
		self.driver = driverQA

	def open_url(self):
		self.driver.get('file://C:/workspace/tdc/sp/2018/python/html/login.html')

	def fill_user(self, value):
		self.driver.send_keys('login', value)

	def fill_password(self, value):
		self.driver.send_keys('password', value)

	def click_ok(self):
		self.driver.click('btnLogin')

	def get_result(self):
		return self.driver.get_text('result')

