#! /usr/bin/env python3


class Solution:
	def computeArea(self, A, B, C, D, E, F, G, H):
		"""
		:type A: int
		:type B: int
		:type C: int
		:type D: int
		:type E: int
		:type F: int
		:type G: int
		:type H: int
		:rtype: int
		"""
		def isRectangleOverlap(rec1, rec2):
			"""
			:type rec1: List[int]
			:type rec2: List[int]
			:rtype: bool
			"""
			newx1 = max(rec1[0], rec2[0])
			newy1 = max(rec1[1], rec2[1])
			newx2 = min(rec1[2], rec2[2])
			newy2 = min(rec1[3], rec2[3])
			if newx1 < newx2 and newy1 < newy2:
				return (newx2 - newx1) * (newy2 - newy1)
			return 0
		rec1 = [A, B, C ,D]
		rec2 = [E, F, G, H]
		total = (C-A) * (D-B)
		total += (G-E) * (H - F)

		return total - isRectangleOverlap(rec1, rec2)

s = Solution()
print( s.computeArea( -3, 0 , 3 , 4 , 0 , -1, 9 , 2 ))

