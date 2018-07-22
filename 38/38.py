#! /usr/bin/env python3
class Solution:
	def countAndSay(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		if n == 1:
			return "1"

		s = ['1']

		def helper(x):
			start = x[0]
			cnt = 0
			while len(x):
				if x[0] == start:
					cnt += 1
					x.pop(0)
				else:
					break
			return start, cnt

		for i in range(n - 1):
			tmp = []
			while len(s) != 0:
				start, cnt = helper(s)
				tmp.extend([str(cnt), start])

			s = tmp
		return "".join(s)

s = Solution()
print(s.countAndSay(4))
