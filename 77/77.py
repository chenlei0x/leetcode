#! /usr/bin/env python3
import copy
class Solution:
	def combine(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[List[int]]
		"""
		
		def _combine(n, k):
			if k == 0:
				return [[]]
			a = [[x] for x in range(1, n+1)]
			for l in range(1, k):
				size = len(a)
				for i in range(size):
					e = a[0]
					for j in range(e[-1] + 1, n + 1):
						tmp = e[::]
						tmp.append(j)
						a.append(tmp)
					a.pop(0)
			return a
		def _r(n, l):
			a = []
			for x in range(1, n+1):
				if x not in l:
					a.append(x)
			return a

		if k < n//2:
			return _combine(n, k)
		a = _combine(n, n - k)
		for i in range(len(a)):
			a[i] = _r(n, a[i])
		return a

def stepm(k):
	ret = 1
	for i in range(1, k+1):
		ret *= i
	return ret

def C(n, k):
	return stepm(n)//stepm(k)//stepm(n-k)


nums = [1,2,3]
s = Solution();
r = s.combine(1, 1)
print(r)

