#! /usr/bin/env python3

class Solution:
	def isToeplitzMatrix(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: bool
		"""
		for i in range(len(matrix) - 1):
			a = matrix[i]
			b = matrix[i+1]
			for j in range(0, len(a) - 1):
				if a[j] != b[j+1]:
					return False

		return True


matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]

s = Solution()
print(s.isToeplitzMatrix(matrix))

