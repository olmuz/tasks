from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatePage:
	def __init__(self, browser):
		self.browser = browser
		self.url = 'http://calcvat.com'
		self.locators = {
						'Calculate': None,
						'fill_sum': None,
						'fill_percent': None,
						'fill_boolen' : None,
						'new_form': None,
					}

	def open(self):
		self.browser.get(self.url)

	def find_element(self, name):
		return self.browser.find_element_by_xpath(self.locators[name])

	@property
	def is_visible(self):
		try:
			WebDriverWait(self.browser, 5).until(
				EC.visibility_of_element_located(
					(By.XPATH, self.locators['new_form'])
				)
			)
		except TimeoutException:
			return False
		else:
			return True