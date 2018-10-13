#! /usr/bin/env python3

class Solution:
	def matrixReshape(self, nums, r, c):
		"""
		:type nums: List[List[int]]
		:type r: int
		:type c: int
		:rtype: List[List[int]]
		"""

		origin_r = len(nums)
		origin_c = len(nums[0])
		if origin_r * origin_c != r * c:
			return nums
		ret =  [[0]*c for i in range(r)]
		print(ret)
		for i in range(r):
			for j in range(c):
				t = i * c + j
				x = t // origin_c
				y = t % origin_c
				print("t = ", t)
				print(i,j, "===", x, y)
				ret[i][j] = nums[x][y]
				print(ret)

		return ret

s = Solution()
nums = [[1,2],
 [3,4]]

ret = s.matrixReshape(nums, 4, 1)
print(ret)
