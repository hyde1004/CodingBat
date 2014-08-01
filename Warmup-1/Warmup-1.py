import unittest

def sleep_in(weekday, vacation):
	if not weekday or vacation:
		return True
	else:
		return False

def monkey_trouble(a_smile, b_smile):
	return not (a_smile != b_smile)

class TestSleepIn(unittest.TestCase):
	def test_sleep_in(self):
		self.assertEqual(sleep_in(False, False), True)
		self.assertEqual(sleep_in(True, False), False)
		self.assertEqual(sleep_in(False, True), True)

	def test_monkey_trouble(self):
		self.assertEqual(monkey_trouble(True, True), True)
		self.assertEqual(monkey_trouble(False, False), True)
		self.assertEqual(monkey_trouble(True, False), False)

if __name__ == "__main__":
	unittest.main()