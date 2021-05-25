class LoginOk:
	def __init__(self, driverQA):
		self.driver = driverQA

	def click_back(self):
		self.driver.click('btnBack')

	def get_result(self):
		return self.driver.get_text('result')