import unittest
from interpreter import tokenize
class Tests(unittest.TestCase):

	def test_one(self):
		self.assertEqual(tokenize("1"),"1")
		self.assertEqual(tokenize("(1)"),["1"])
		self.assertEqual(tokenize("(+ 1 1 (+ 2 3) )"),["+","1","1",["+", "2", "3"]])