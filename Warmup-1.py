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

def diff21(n):
	# if n > 21:
	# 	return abs(21 - n) * 2
	# else:
	# 	return abs(21 - n)

	diff = abs(21 - n)
	if n > 21:
		diff *= 2
	return diff
	
def parrot_trouble(talking, hour):
	# if talking and ( hour < 7 or hour > 20):
	# 	return True
	# else:
	# 	return False

	return talking and ( hour < 7 or hour > 20)

def makes10(a, b):
	#	return True

	# if (a == 10 or b == 10) or a + b == 10:
	# 	return True
	# else:
	# 	return False

	return (a == 10 or b == 10) or a + b == 10

def near_hundred(n):
	return (abs(n - 100) <= 10) or (abs(n - 200) <= 10)

def pos_neg(a, b, negative):
	# return (a * b < 0) or (negative == True and (a < 0 and b < 0))

	# if negative == True:
	# 	return a < 0 and b < 0
	# else:
	# 	return (a * b < 0) 

	return (a < 0 and b < 0) if negative else (a * b < 0)

def not_string(str):
	# return "not " + str
	if str[0:3] == "not":
		return str
	else:
		return "not " + str
		
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

	def test_diff21(self):
		self.assertEqual(diff21(19), 2)
		self.assertEqual(diff21(10), 11)
		self.assertEqual(diff21(21), 0)

	def test_parrot_trouble(self):
		self.assertEqual(parrot_trouble(True, 6), True)
		self.assertEqual(parrot_trouble(True, 7), False)
		self.assertEqual(parrot_trouble(False, 6), False)

	def test_makes10(self):
		self.assertEqual(makes10(9, 10), True)
		self.assertEqual(makes10(9, 9), False)
		self.assertEqual(makes10(1, 9), True)

	def test_near_hundred(self):
		self.assertEqual(near_hundred(93), True)
		self.assertEqual(near_hundred(90), True)
		self.assertEqual(near_hundred(89), False)

	def test_pos_neg(self):
		self.assertEqual(pos_neg(1, -1, False), True)
		self.assertEqual(pos_neg(-1, 1, False), True)
		self.assertEqual(pos_neg(-4, -5, True), True)

	def test_not_string(self):
		self.assertEqual(not_string('candy'), 'not candy')
		self.assertEqual(not_string('x'), 'not x')
		self.assertEqual(not_string('not bad'), 'not bad')


if __name__ == "__main__":
	unittest.main()