import unittest

def string_times(str, n):
	return str * n

class TestWarmUp2(unittest.TestCase):
	def test_string_times(self):
		self.assertEqual(string_times('Hi', 2), 'HiHi')
		self.assertEqual(string_times('Hi', 3), 'HiHiHi')
		self.assertEqual(string_times('Hi', 1), 'Hi')

if __name__ == "__main__":
	unittest.main()