#! /usr/bin/env python3
class Solution:
	def rotate(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		length = len(matrix)

		for x in range(length):
			for y in range(x):
				matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

		print(matrix)
		for l in matrix:
			for i in range(0, length//2):
				l[i] ,l[-1 - i] = l[-1 - i], l[i]



matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

s = Solution()
s.rotate(matrix)
print(matrix)


