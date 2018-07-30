#! /usr/bin/env python3

class Solution:
	def isRectangleOverlap(self, rec1, rec2):
		"""
		:type rec1: List[int]
		:type rec2: List[int]
		:rtype: bool
		"""
		newx1 = max(rec1[0], rec2[0])
		newy1 = max(rec1[1], rec2[1])
		newx2 = max(rec2[2], rec2[2])
		newy2 = max(rec2[3], rec2[3])
		return newx1 < newx2 and newy1 < newy2
