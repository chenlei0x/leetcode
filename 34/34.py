#! /usr/bin/env python3

class Solution:
	def searchRange(self, nums, target):
		"""
		:type nums: List[int]
		 :type target: int
		 :rtype: List[int]
		"""
		left = 0
		right = len(nums) - 1
		while (left < right):
			mid = (left + right)//2
			if nums[mid] > target:
				right = mid - 1;
			elif nums[mid] < target:
				left = mid + 1;
			else:
				ret = [mid, mid]
				while(ret[0] - 1 >= 0 and nums[ret[0] - 1] == target):
					ret[0] -= 1
				while(0 <= ret[1] + 1 < len(nums) and nums[ret[1] + 1] == target):
					ret[1] += 1
				return ret
		if left == right and nums[left] == target:
			return [left, left]
		return [-1, -1]	

s = Solution()
test =  [2 ,2]
targets = [2]

for i in targets:
	ret = s.searchRange(test, i)
	print(ret)
