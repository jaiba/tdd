from unittest import skip
from functional_tests.base import FunctionalTest

class ItemValidationTest(FunctionalTest):
  
  def test_cannot_add_empty_list_items(self):
    # On going to the home page I accidentally hit enter before typing anything
    
    # The page refreshes showing an error message that blank list items are not
    # allowed
    
    # I try again but enter some text this time and everything works
    
    # Stupid me, I again hit enter with a blank input box
    
    # The page refreshes again to reveal another error message
    
    # I correct the mistake by entering some text
    self.fail('Write Me!')