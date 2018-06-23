#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Solution:
	def removeDuplicates(self, nums):
		if (len(nums) <= 2):
			return len(nums)
		
		m = 0
		what = nums[0]
		count = 1
		for i in range(1, len(nums)):
			e = nums[i]
			if e != what:
				for i in range(min(count, 2)):
					nums[m] = what
					m += 1
				what = e
				count = 1
			else:
				count +=1

		for i in range(min(count, 2)):
			nums[m] = what
			m += 1
		del nums[m:]

nums = []
s = Solution()
s.removeDuplicates(nums)
print(nums)
