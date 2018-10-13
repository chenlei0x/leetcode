#! /usr/bin/env python3

class Solution:
	def projectionArea(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		top=sum(sum(1 for j in i if j) for i in grid)
		left=sum(max(i) for i in grid)
		front=sum(max(i) for i in zip(*grid))
		return top+left+front
