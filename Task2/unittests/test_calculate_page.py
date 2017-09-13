import unittest
from selenium import webdriver
from calculate_page import CalculatePage

class TestCalculatePage(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.browser = webdriver.Chrome()

	def setUp(self):
		CalculatePage(self.browser).open()

	def test_check_elements(self):
		for i in self.locators.keys():
			try:
				CalculatePage(self.browser).find_element(i)
			except:
				raise Exception('element not found')


	def check_calculations(self):
		pass


	def tearDown(self):
		CalculatePage(self.browser).close()