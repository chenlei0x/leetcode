#! /usr/bin/env python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def insertIntoBST(self, root, val):
		"""
		:type root: TreeNode
		:type val: int
		:rtype: TreeNode
		"""
		n = root
		while n is not None:
			if val > n.val:
				if n.right is None:
					new = TreeNode(val)
					n.right = new
					return root
				else:
					n = n.right
			elif val < n.val:
				if n.left is None:
					new = TreeNonde(val)
					n.left = new
					return root
				else:
					n = n.left
		return root
