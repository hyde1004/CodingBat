import unittest
def sleep_in(weekday, vacation):
	if not weekday or vacation:
		return True
	else:
		return False

class TestSleepIn(unittest.TestCase):
	def test_sleep_in(self):
		self.assertEqual(sleep_in(False, False), True)
		self.assertEqual(sleep_in(True, False), False)
		self.assertEqual(sleep_in(False, True), True)


if __name__ == "__main__":
	unittest.main()