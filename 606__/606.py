#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def create(self, l):
		if not len(l):
			return
		root = TreeNode(l.pop(0))
		tmp_list = [root]
		while(len(l)):
			size = tmp_list.__len__()
			while(size > 0):
				t = tmp_list.pop(0)
				size -= 1
				if not len(l):
					return root
				t.left = TreeNode(l.pop(0))
				tmp_list.append(t.left)

				if not len(l):
					return root
				t.right = TreeNode(l.pop(0))
				tmp_list.append(t.right)
		return root

	def print_tree(self, root):
		def _print(root):
			if not root:
				return
			print(root.val)
			_print(root.left)
			_print(root.right)
		_print(root)

	def tree2str(self, t):
		"""
		:type t: TreeNode
		:rtype: str
		"""

		def _tree2str(t):
			if not t or t.val is None:
				return ""
			if t.right:
				f = "{}({})({})".format(t.val, _tree2str(t.left), _tree2str(t.right))
				return f
			if t.left:
				f = "{}({})".format(t.val, _tree2str(t.left))
				return f
			else:
				return str(t.val)


		ret = _tree2str(t)
		print(ret)
		return ret

s = Solution()
root = s.create([0])
s.print_tree(root)
ret = s.tree2str(root)
