#! /usr/bin/env python3

class Solution:
	def transpose(self, A):
		"""
		:type A: List[List[int]]
		:rtype: List[List[int]]
		"""
		ret = []
		for i in zip(*A):
			print(i)
			ret.append(list(i))
		return ret

s = Solution()
ret = s.transpose([[1,2,3],[4,5,6],[7,8,9]])
print(ret)
