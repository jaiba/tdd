from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)
		
  def tearDown(self):
    self.browser.quit()
    
  def check_for_row_in_list_table(self, row_text):
    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertIn(row_text, [row.text for row in rows])
		
  def test_can_start_a_list_and_retrieve_it_later(self):

    # I'm making a to-do list app to motivate myself. Here's where I go to look at it.
    self.browser.get(self.live_server_url)

    # I should see the page title reinforce that I'm looking at a to-do list
    self.assertIn('To-Do', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('To-Do', header_text)

    # I'm invited to enter a to-do item at the home page
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
    )

    # I can type "Learn tdd" into a text box
    inputbox.send_keys('Learn tdd')

    # After hitting enter, the page updates and now it shows
    # "1: Learn tdd" as an item on a to-do list
    inputbox.send_keys(Keys.ENTER)

    self.check_for_row_in_list_table('1: Learn tdd')
    
    # There is still a text box in which to enter more to-dos.
    # I enter "Build bead stringing app"
    inputbox = self.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('Build bead stringing app')
    inputbox.send_keys(Keys.ENTER)

    # The page updates again and now shows two items on my list
    self.check_for_row_in_list_table('1: Learn tdd')
    self.check_for_row_in_list_table('2: Build bead stringing app')

    # Wondering how I'll get back to the list, I see that the 
    # site has generated a unique URL for me to visit to retrieve
    # the list because the site offers some text explaining that
    self.fail('Finish the test!')
    # I visit that URL and see my list
    