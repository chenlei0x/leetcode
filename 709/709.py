#! /usr/bin/env python3
class Solution:
	def toLowerCase(self, __str):
		"""
		:type str: str
		:rtype: str
		"""

		_str = list(__str)
		for i in range(len(_str)):
			if ord('A') <= ord(_str[i]) <= ord('Z'):
				diff = ord('a') - ord('A')
				_str[i] = chr(ord(_str[i]) + diff)

		return "".join(_str)

s = Solution()
s.toLowerCase("Hwwll")
