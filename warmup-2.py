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

def last2(str):
	return 1

def array_count9(nums):
	return nums.count(9)

def array_front9(nums):
	return nums[:4].count(9) > 0

def array123(nums):
	return nums.count(1) > 0 and nums.count(2) > 0 and nums.count(3) > 0

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

	def test_last2(self):
		self.assertEqual(last2('hixxhi'), 1)

	def test_array_count9(self):
		self.assertEqual(array_count9([1, 2, 9]), 1)
		self.assertEqual(array_count9([1, 9, 9]), 2)
		self.assertEqual(array_count9([1, 9, 9, 3, 9]), 3)

	def test_array_front9(self):
		self.assertEqual(array_front9([1, 2, 9, 3, 4]), True)
		self.assertEqual(array_front9([1, 2, 3, 4, 9]), False)
		self.assertEqual(array_front9([1, 2, 3, 4, 5]), False)

	def test_array123(self):
		self.assertEqual(array123([1, 1, 2, 3]), True)
		self.assertEqual(array123([1, 1, 2, 4, 1]), False)
		self.assertEqual(array123([1, 1, 2, 1, 2, 3]), True)

if __name__ == "__main__":
	unittest.main()