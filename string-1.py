import unittest

def hello_name(name):
	return 'Hello ' + name + '!'

def make_abba(a, b):
	return a + b + b + a

def make_tags(tag, word):
	return '<' + tag + '>' + word + '</' + tag + '>'

def make_out_word(out, word):
	return out[:2] + word + out[2:]

def extra_end(str):
#	return (str[-2] + str[-1]) * 3
	return str[-2:] * 3
	
def first_two(str):
	return str[:2]

def first_half(str):
	return str[:len(str)//2]

class TestString1(unittest.TestCase):
	def test_hello_name(self):
		self.assertEqual(hello_name('Bob'), 'Hello Bob!')
		self.assertEqual(hello_name('Alice'), 'Hello Alice!')
		self.assertEqual(hello_name('X'), 'Hello X!')

	def test_make_abba(self):
		self.assertEqual(make_abba('Hi', 'Bye'), 'HiByeByeHi')
		self.assertEqual(make_abba('Yo', 'Alice'), 'YoAliceAliceYo')
		self.assertEqual(make_abba('What', 'Up'), 'WhatUpUpWhat')

	def test_make_tags(self):
		self.assertEqual(make_tags('i', 'Yay'), '<i>Yay</i>')
		self.assertEqual(make_tags('i', 'Hello'), '<i>Hello</i>')
		self.assertEqual(make_tags('cite', 'Yay'), '<cite>Yay</cite>')

	def test_make_out_word(self):
		self.assertEqual(make_out_word('<<>>', 'Yay'), '<<Yay>>')
		self.assertEqual(make_out_word('<<>>', 'WooHoo'), '<<WooHoo>>')
		self.assertEqual(make_out_word('[[]]', 'word'), '[[word]]')

	def test_extra_end(self):
		self.assertEqual(extra_end('Hello'), 'lololo')
		self.assertEqual(extra_end('ab'), 'ababab')
		self.assertEqual(extra_end('Hi'), 'HiHiHi')

	def test_first_two(self):
		self.assertEqual(first_two('Hello'), 'He');
		self.assertEqual(first_two('abcdefg'), 'ab');
		self.assertEqual(first_two('ab'), 'ab');

	def test_first_half(self):
		self.assertEqual(first_half('WooHoo'), 'Woo')
		self.assertEqual(first_half('HelloHello'), 'Hello')
		self.assertEqual(first_half('abcdef'), 'abc')
		
if __name__ == "__main__":
	unittest.main()