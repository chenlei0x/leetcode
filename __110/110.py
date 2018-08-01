#! /usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def isBalanced(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		heights = []
		def helper(root, height):
			if root is None:
				return
			if root.left is None or root.right is None:
				print(root.val)
				heights.append(height)
			helper(root.left, height + 1)
			helper(root.right, height + 1)
		helper(root, 1)
		print(heights)
		return len(heights) == 0 or max(heights) - min(heights) <= 1

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def main():
	line = "[1,2,2,3,3,3,3,4,4,4,4,4,4,null,null,5,5]"
	root = stringToTreeNode(line);

	ret = Solution().isBalanced(root)

	out = (ret);
	print(out)

if __name__ == '__main__':
    main()
