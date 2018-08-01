#! /usr/bin/env python3

class Solution:
	def arrayPairSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums.sort()

		sum = 0
		for x in range(0, len(nums), 2):
			sum += num[x]
		return sum
s = Solution();
print(s.generateParenthesis(3))

