#! /usr/bin/env python3



class Solution:
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		ret = []
		def generate(s, left, right):
			if len(s) == 2*n:
				ret.append(s)
			if left < n:
				generate(s + '(', left + 1, right)
			if right < left:
				generate(s + ')', left, right + 1)

		generate("", 0, 0)
		return ret

s = Solution();
print(s.generateParenthesis(3))

