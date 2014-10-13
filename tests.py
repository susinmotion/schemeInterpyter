import unittest
from interpreter import tokenize, findInnerMost, operate, evaluate, listify, operators, let
class Tests(unittest.TestCase):

	def test_let(self):
		print operate(findInnerMost(listify ("( + x u )")))
		self.assertEqual(evaluate("(let ((x 2) (u 50)) (+ x u)"),52)
"""	def test_tokenize(self):
		#self.assertEqual(tokenize("1"),"1")
		#self.assertEqual(("( 1 )"),[1])
		self.assertEqual(listify("(+ 1 1 (+ 2 3) )"),["+","1","1",["+", "2", "3"]])
		self.assertEqual(listify("(+ 1 (+ 1 (+ 1 1) 2) 3 (+ 2 2) 5)))"),["+","1",["+","1",["+","1","1"], "2"], "3" ,["+", "2","2"], "5"])

	def test_adD(self):
		self.assertEqual(evaluate("(+ 1 (+ 1 (+ 1 1) 2) 3 (+ 2 2) 5)))"),18)
	def test_adD(self):
		self.assertEqual(evaluate("(+ 1 (+ 1 (+ 1 1) 2) 3 (+ 2 2) 5)))"),18)

	def test_sqare(self):
		operate(listify("(define (square x) (* x x) )"))
		self.assertEqual(evaluate("(square 2)"), 4)
	


	def test_complex(self):
		operate(listify("(define (f x) (* x x (+ 5 x) ) )"))
		self.assertIn("f", operators)
		self.assertEqual(evaluate("(f 2)"), 28)"""
