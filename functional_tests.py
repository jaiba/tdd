from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		
	def tearDown(self):
		self.browser.quit()
		
	def test_can_start_a_list_and_retrieve_it_later(self):

		# I'm making a to-do list app to motivate myself. Here's where I go to look at it.
		self.browser.get('http://localhost:8000')

		# I should see the page title reinforce that I'm looking at a to-do list
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# I'm invited to enter a to-do item at the home page

		# I can type "Learn tdd" into a text box

		# After hitting enter, the page updates and now it shows
		# "1: Learn tdd" as an item on a to-do list

		# There is still a text box in which to enter more to-dos.
		# I enter "Build bead stringing app"

		# The page updates again and now shows two items on my list

		# Wondering how I'll get back to the list, I see that the 
		# site has generated a unique URL for me to visit to retrieve
		# the list because the site offers some text explaining that

		# I visit that URL and see my list

if __name__ == '__main__':
	unittest.main(warnings = 'ignore')