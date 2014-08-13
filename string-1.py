import unittest

def hello_name(name):
	return 'Hello ' + name + '!'

class TestString1(unittest.TestCase):
	def test_hello_name(self):
		self.assertEqual(hello_name('Bob'), 'Hello Bob!')
		self.assertEqual(hello_name('Alice'), 'Hello Alice!')
		self.assertEqual(hello_name('X'), 'Hello X!')

		pass
if __name__ == "__main__":
	unittest.main()