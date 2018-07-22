#! /usr/bin/env python3
import copy
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

	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		ret = []
		nums.sort()
		ret.append(copy.deepcopy(nums))

		while True:
			for i in range(len(nums) - 1, 0, -1):
				if nums[i-1] < nums[i]:
					dummy = i - 1
					break
			else:
				return ret

			for i in range(len(nums) - 1, dummy, -1):
				if (nums[i] > nums[dummy]):
					foo = i
					break;

			nums[dummy], nums[foo] = nums[foo], nums[dummy]
			nums[dummy + 1:] = nums[dummy + 1:][::-1]
			ret.append(copy.deepcopy(nums))

nums = [1,2,3]
s = Solution();
r = s.permute(nums)
print(r)

