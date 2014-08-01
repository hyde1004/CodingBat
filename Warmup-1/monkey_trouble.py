import unittest

def monkey_trouble(a_smile, b_smile):
	return not (a_smile != b_smile)

class TestMonkeyTrouble(unittest.TestCase):
	def test_monkey_trouble(self):
		self.assertEqual(monkey_trouble(True, True), True)
		self.assertEqual(monkey_trouble(False, False), True)
		self.assertEqual(monkey_trouble(True, False), False)

if __name__ == "__main__":
	unittest.main()