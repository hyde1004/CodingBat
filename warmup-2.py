import unittest

def string_times(str, n):
	return str * n

def front_times(str, n):	
	return str[:3] * n

def string_bits(str):
	return str[::2]

def string_splosion(str):
	splosion = ''

	for i in range(len(str)+1):
		splosion += str[:i]

	return splosion

class TestWarmUp2(unittest.TestCase):
	def test_string_times(self):
		self.assertEqual(string_times('Hi', 2), 'HiHi')
		self.assertEqual(string_times('Hi', 3), 'HiHiHi')
		self.assertEqual(string_times('Hi', 1), 'Hi')

	def test_front_times(self):
		self.assertEqual(front_times('Chocolate', 2), 'ChoCho')
		self.assertEqual(front_times('Chocolate', 3), 'ChoChoCho')
		self.assertEqual(front_times('Abc', 3), 'AbcAbcAbc')

	def test_string_bits(self):
		self.assertEqual(string_bits('Hello'), 'Hlo')
		self.assertEqual(string_bits('Hi'), 'H')
		self.assertEqual(string_bits('Heeololeo'), 'Hello')
		
	def test_string_splosion(self):
		self.assertEqual(string_splosion('Code'), 'CCoCodCode')
		self.assertEqual(string_splosion('abc'), 'aababc')
		self.assertEqual(string_splosion('ab'), 'aab')

if __name__ == "__main__":
	unittest.main()