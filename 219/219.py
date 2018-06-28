#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Solution:
	def containsNearbyDuplicate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		d = {}
		for i,n in enumerate(nums):
			if i - d.get(n, -k-1) < k:
				return True
			d[n] = i
		return False


nums = [1,2,3,1,2,3]

k = 2
s = Solution()
print(s.containsNearbyDuplicate(nums, k))

