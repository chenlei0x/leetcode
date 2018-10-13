#! /usr/bin/env python3

class Solution:
	def selfDividingNumbers(self, left, right):
		"""
		:type left: int
		:type right: int
		:rtype: List[int]
		"""
		res = []
		for i in range(left, right + 1):
			cur = i
			while cur != 0:
				digit = cur % 10
				if digit == 0:
					break
				cur = cur// 10
				if i % digit != 0:
					break
			else:
				res.append(i)
		return res
s = Solution()
s.selfDividingNumbers(1, 22)
