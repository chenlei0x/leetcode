#! /usr/bin/env python3
class Solution:
	def searchBST(self, root, val):
		"""
		:type root: TreeNode
		:type val: int
		:rtype: TreeNode
		"""
		n = root
		while not n is None:
			if val == n.val:
				return n
			if val > n.val:
				n = n.right
			elif val < n. val:
				n = n.left
		return None
