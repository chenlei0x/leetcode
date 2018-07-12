#! /usr/bin/env python3

class Solution:
	def minCostClimbingStairs(self, cost):
		"""
		:type cost: List[int]
		:rtype: int
		"""
		a = [0] * (len(cost) + 1)
		for i in range(2, len(cost) + 1):
			a[i] = min(a[i-1] + cost[i-1], a[i-2] + cost[i-2])
		return a[-1]

s = Solution()
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(s.minCostClimbingStairs(cost))


