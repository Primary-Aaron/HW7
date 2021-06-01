import unittest
import fizzBuzz

class test_(unittest.TestCase):
  def test_average1(self):
    fizzy = fizzBuzz.fizzBuzz(3)
    message = "this ain't it, chief"
    self.assertIsInstance(fizzy, list, message)