import unittest
import leapYear

class test_(unittest.TestCase):
  def test_4(self):
    year = leapYear.isLeapYear(8)
    message = "this ain't it, chief"
    self.assertEqual(year, True, message)
#  def test_100(self):
#    fizzy = fizzBuzz.fizzBuzz()
#    buzzy = [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz", 13, 14, "fizzbuzz"]
#    #message = "this ain't it, chief"
#    self.assertEqual(fizzy, buzzy)