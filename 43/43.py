#! /usr/bin/env python3
class Solution:
	def multiply(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		if (num1 == '0' or num2 == '0'):
			return "0"

		def multiplier(num, m):
			carry = 0
			ret = []
			for i in num[::-1]:
				res = int(m) * int(i) + carry
				carry = res//10
				res = res%10
				ret.insert(0, res)
			if carry != 0:
				ret.insert(0, carry)

			return ret

		def adder(num1, num2):
			carry = 0
			ret = []
			num1 = num1[::-1]
			num2 = num2[::-1]
			i1 = 0
			i2 = 0

			for i in range(max(len(num1), len(num2))):
				add1 = num1[i] if i < len(num1) else 0
				add2 = num2[i] if i < len(num2) else 0
				res = int(add1) + int(add2) + carry
				carry = res//10
				res = res%10
				ret.insert(0, res)
			if carry != 0:
				ret.insert(0, carry)

			return ret

		ret = []
		for i in range(len(num2)):
			m = num2[-1]
			num2 = num2[0:-1]
			res = multiplier(num1, m)
			res.extend([0] * i)
			ret = adder(ret, res)

		ret = list(map(str, ret))
		return "".join(ret)

s = Solution()
print(s.multiply("123", "456"))
