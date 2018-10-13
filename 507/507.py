#! /usr/bin/env python3

class Solution:
	def checkPerfectNumber(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		if num <= 1:
			return False
		t = 1
		for i in range(2, int(num**0.5) + 1):
			if num % i == 0:
				t += i
				t += num//i
				print(t)
		return t == num

s = Solution()
res = s.checkPerfectNumber(28)
print(res)
