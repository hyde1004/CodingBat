import unittest

def sleep_in(weekday, vacation):
	if not weekday or vacation:
		return True
	else:
		return False

def monkey_trouble(a_smile, b_smile):
	return not (a_smile != b_smile)

def sum_double(a, b):
	if a == b:
		return (a + b) * 2
	else:
		return (a + b)

	# sum = a + b
	# if a == b:
	# 	sum *= 2
	# return sum

class TestSleepIn(unittest.TestCase):
	def test_sleep_in(self):
		self.assertEqual(sleep_in(False, False), True)
		self.assertEqual(sleep_in(True, False), False)
		self.assertEqual(sleep_in(False, True), True)

	def test_monkey_trouble(self):
		self.assertEqual(monkey_trouble(True, True), True)
		self.assertEqual(monkey_trouble(False, False), True)
		self.assertEqual(monkey_trouble(True, False), False)

	def test_sum_double(self):
		self.assertEqual(sum_double(1, 2), 3)
		self.assertEqual(sum_double(3, 2), 5)
		self.assertEqual(sum_double(2, 2), 8)

if __name__ == "__main__":
	unittest.main()