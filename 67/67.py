#! /usr/bin/env python3
class Solution:
	def addBinary(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""
		carry = 0
		ret = []
		a = list(a)
		b = list(b)
		while len(a) or len(b):
			_a, _b = 0, 0	
			if len(a):
				_a = int(a.pop())
			if len(b):
				_b = int(b.pop())
			result = _a + _b + carry
			if result > 1:
				carry = 1
				result -= 2
			else:
				carry = 0
			ret.insert(0, str(result))
		if carry != 0:
			ret.insert(0, str(carry))
		return "".join(ret)

s = Solution()
a = "1111"
b = "1"
s.addBinary(a, b)
