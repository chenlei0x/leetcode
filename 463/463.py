#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Solution:
	def islandPerimeter(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		ret = 0
		m = len(grid)
		n = len(grid[0])
		grid.insert(0, [0]*n)
		grid.append([0]*n)
		for i in grid:
			i.insert(0, 0)
			i.append(0)
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == 0:
					continue
				tmp = 0
				if grid[i+1][j] == 0:
					tmp += 1
				if grid[i-1][j] == 0:
					tmp += 1
				if grid[i][j+1] == 0:
					tmp += 1
				if grid[i][j-1] == 0:
					tmp += 1
				ret += tmp
		return ret

s = Solution()
M = [[0,1,0,0],
	 [1,1,1,0],
	 [0,1,0,0],
	 [1,1,0,0]]
s.islandPerimeter(M)
