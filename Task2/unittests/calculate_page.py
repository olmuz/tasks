class CalculatePage:
	def __init__(self, browser):
		self.browser = browser
		self.url = 'http://calcvat.com'
		self.locators = {
						'Calculate': None,
						'fill_sum': None,
						'fill_percent': None,
						'fill_boolen' : None,
						'new_form' : None,
						'new_form_result': None
					}

	def open(self):
		self.browser.get(self.url)

	def find_element(self, name):
		return self.browser.find_element_by_xpath(self.locators[name])