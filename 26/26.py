#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Solution:
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if (len(nums) <= 1):
			return len(nums)

		m = t = None
		for i in range(len(nums) - 1):
			if nums[i] == nums[i+1]:
				m = i
				t = i + 1
				break
		if m is None:
			return len(nums)

		m += 1
		t += 1
		while t < len(nums):
			if nums[m - 1] == nums[t]:
				t += 1
			else:
				nums[m] = nums[t]
				m += 1
		del nums[m:]
		return len(nums)


nums = [0,0,0,0,0,111111111111,11,11,11,11]
s = Solution()
s.removeDuplicates(nums)
print(nums)
