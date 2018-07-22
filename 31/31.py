#! /usr/bin/env python3
class Solution:
	def nextPermutation(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		for i in range(len(nums) - 1, 0, -1):
			if  nums[i-1] < nums[i]:
				break
		else:
			nums = nums.reverse()
			return
		dummy = i - 1
		print("dummy = {}".format(dummy))

		for j in range(len(nums) - 1, dummy, -1):
			if nums[j] > nums[dummy]:
				foo = j
				break
		else:
			foo = dummy
		print("foo = {}".format(foo))

		nums[dummy], nums[foo] = nums[foo], nums[dummy]
		nums[dummy + 1:] = nums[dummy + 1:][::-1]


nums = [3,2,1]
s = Solution();
s.nextPermutation(nums)
print(nums)

