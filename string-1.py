import unittest

def hello_name(name):
	return 'Hello ' + name + '!'

def make_abba(a, b):
	return a + b + b + a

class TestString1(unittest.TestCase):
	def test_hello_name(self):
		self.assertEqual(hello_name('Bob'), 'Hello Bob!')
		self.assertEqual(hello_name('Alice'), 'Hello Alice!')
		self.assertEqual(hello_name('X'), 'Hello X!')

	def test_make_abba(self):
		self.assertEqual(make_abba('Hi', 'Bye'), 'HiByeByeHi')
		self.assertEqual(make_abba('Yo', 'Alice'), 'YoAliceAliceYo')
		self.assertEqual(make_abba('What', 'Up'), 'WhatUpUpWhat')

if __name__ == "__main__":
	unittest.main()