import unittest

def first_last6(nums):
	return (nums[0] == 6 or nums[-1] == 6)

def same_first_last(nums):
	return nums[0] == nums[-1]

def make_pi():
	return [3, 1, 4]
	
def common_end(a, b):
	return (a[0] == b[0] or a[-1] == b[-1])

def sum3(nums):
	return sum(nums)

def rotate_left3(nums):
	return nums[1:] + nums[0:1]

class TestList1(unittest.TestCase):
	def test_first_last6(self):
		self.assertEqual(first_last6([1, 2, 6]), True)

	def test_same_first_last(self):
		self.assertEqual(same_first_last([1, 2, 3]), False)
		self.assertEqual(same_first_last([1, 2, 3, 1]), True)
		self.assertEqual(same_first_last([1, 2, 1]), True)

	def test_make_pi(self):
		self.assertEqual(make_pi(), [3, 1, 4])

	def test_common_end(self):
		self.assertEqual(common_end([1, 2, 3], [7, 3]), True)
		self.assertEqual(common_end([1, 2, 3], [7, 3, 2]), False)
		self.assertEqual(common_end([1, 2, 3], [1, 3]), True)

	def test_sum3(self):
		self.assertEqual(sum3([1, 2, 3]), 6)
		self.assertEqual(sum3([5, 11, 2]), 18)
		self.assertEqual(sum3([7, 0, 0]), 7)

	def test_rotate_left3(self):
		self.assertEqual(rotate_left3([1, 2, 3]), [2, 3, 1])
		self.assertEqual(rotate_left3([5, 11, 9]), [11, 9, 5])
		self.assertEqual(rotate_left3([7, 0, 0]), [0, 0, 7])

if __name__ == "__main__":
	unittest.main()