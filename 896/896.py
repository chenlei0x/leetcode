#! /usr/bin/env python3

class Solution:
	def isMonotonic(self, A):
		"""
		:type A: List[int]
		:rtype: bool
		"""
		if A[-1] == A[0]:
			for i in range(len(A)):
				if A[i] != A[0]:
					return False
			return True
		if A[0] > A[-1]:
			for i in range(len(A) - 1):
				if A[i] < A[i+1]:
					return False
			return True
		if A[0] < A[-1]:
			for i in range(len(A) - 1):
				if A[i] > A[i+1]:
					return False
			return True


