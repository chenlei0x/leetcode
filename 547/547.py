#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import ipdb
class Solution:
	def findCircleNum(self, M):
		"""
		:type M: List[List[int]]
		:rtype: int
		"""
		visited = []
		ret = 0
		def find_friends(x):
			ret = []
			for i in range(len(M)):
				if i != x and not i in visited and M[x][i] == 1:
					ret.append(i)
			return ret

		for t in range(len(M)):
			circle = []
			if t in visited:
				continue
			circle.append(t)

			while len(circle):
				t = circle.pop(0)
				visited.append(t)
				friends = find_friends(t)
				if len(friends) == 0:
					continue
				circle.extend(friends)
			ret += 1

		return ret

class Solution1:
	def findCircleNum(self, M):
		"""
		:type M: List[List[int]]
		:rtype: int
		"""

		visited = {}
		ret = 0
		def find_friends(x):
			ret = []
			for i in range(len(M)):
				if i != x and not visited.get(i, False) and M[x][i] == 1:
					ret.append(i)
			return ret


		for s in range(len(M)):
			circle = []
			if visited.get(s, False):
				continue
			circle.append(s)
			visited[s] = True
			while len(circle):
				t = circle.pop(0)
				for i in range(len(M)):
					if i != t and M[t][i] == 1 and not visited.get(i, False):
						circle.append(i)
						visited[i] = True
			ret += 1

		return ret


s = Solution1()
M = [[1,1,0],[1,1,0],[0,0,1]]
print(s.findCircleNum(M))
