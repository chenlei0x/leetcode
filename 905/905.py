#! /usr/bin/env python3

class Solution:
	def sortArrayByParity(self, A):
		"""
		:type A: List[int]
		:rtype: List[int]
		"""
		a = A
		i = 0
		j = len(a) - 1
		while i < j:
			while a[i] % 2 == 0 and i < j:
				i += 1
			
			while a[j] % 2 != 0 and i < j:
				j -= 1
			
			if not i < j:
				break
			a[i], a[j] = a[j], a[i]
		print(a)
		return a


t = [3,1,2,4, 2,5,6,7,2,3]
s = Solution()
s.sortArrayByParity(t)
