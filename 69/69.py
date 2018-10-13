#! /usr/bin/env python3

class Solution:
	def mySqrt(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		i = 0
		j = x
		while i <= j:
			mid = (i + j) // 2
			print(mid)
			if mid**2 <= x < (mid + 1)**2:
				return mid

			if mid**2 > x:
				j = mid - 1
			else:
				i = mid + 1
			print(i, j)
			print("===")

		return mid
s = Solution()
x = s.mySqrt(4)
print(x)
