import unittest

def first_last6(nums):
	return (nums[0] == 6 or nums[-1] == 6)

def same_first_last(nums):
	return nums[0] == nums[-1]

def make_pi():
	return [3, 1, 4]
	
class TestList1(unittest.TestCase):
	def test_first_last6(self):
		self.assertEqual(first_last6([1, 2, 6]), True)

	def test_same_first_last(self):
		self.assertEqual(same_first_last([1, 2, 3]), False)
		self.assertEqual(same_first_last([1, 2, 3, 1]), True)
		self.assertEqual(same_first_last([1, 2, 1]), True)

	def test_make_pi(self):
		self.assertEqual(make_pi(), [3, 1, 4])

if __name__ == "__main__":
	unittest.main()