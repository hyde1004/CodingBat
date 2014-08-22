import unittest

def first_last6(nums):
	return (nums[0] == 6 or nums[-1] == 6)


class TestList1(unittest.TestCase):
	def test_first_last6(self):
		self.assertEqual(first_last6([1, 2, 6]), True)

if __name__ == "__main__":
	unittest.main()