import unittest
import fizzBuzz

class test_(unittest.TestCase):
  def test_type(self):
    fizzy = fizzBuzz.fizzBuzz()
    message = "this ain't it, chief"
    self.assertIsInstance(fizzy, list, message)
  def test_contents(self):
    fizzy = fizzBuzz.fizzBuzz()
    buzzy = [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz", 13, 14, "fizzbuzz"]
    #message = "this ain't it, chief"
    self.assertEqual(fizzy, buzzy)