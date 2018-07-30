#! /usr/bin/env python3
class Solution:
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""

		if len(prices) == 0:
			return 0
		m = prices[0]
		d = 0
		for i in range(1, len(prices)):
			if prices[i] < m:
				m = prices[i]
			t = prices[i] - m
			if t > d:
				d = t
		return d

l = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit(l))
