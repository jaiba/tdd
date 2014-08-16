from django.test import TestCase

# Test test
class SmokeTest(TestCase):

  def test_bad_maths(self):
    self.assertEqual(1 + 1, 3)
