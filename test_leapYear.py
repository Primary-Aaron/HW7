import unittest
import leapYear

class test_(unittest.TestCase):
  def test_4(self):
    year = leapYear.isLeapYear(8)
    message = "this ain't it, chief"
    self.assertEqual(year, True, message)
  def test_100(self):
    year = leapYear.isLeapYear(200)
    #message = "this ain't it, chief"
    self.assertEqual(year, False)