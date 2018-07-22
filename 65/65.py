#! /usr/bin/env python3


class Solution:
	def isNumber(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		state_machine = [
			{'.': 2, 'blank': 0, 'sign':0, 'digit':1},
			{"digit": 1, 'e': 4, 'blank': 6, '.':3},
			{ 'digit':3},
			{'digit':3, 'e':4, 'blank':6},
			{'digit':5},
			{'digit':5, 'blank': 6},
			{'blank': 6},
		]
		cur_state = 0
		digit_list = [chr(x) for x in range(ord('0'), ord('9') + 1)]
		for i in s:
			if i == ' ':
				c = 'blank'
			elif i in ['+', '-']:
				c = 'sign'
			elif i in digit_list:
				c = 'digit'
			else:
				c = i

			if c in state_machine[cur_state]:
				cur_state = state_machine[cur_state][c]
			else:
				return False

		if 'blank' in state_machine[cur_state].keys() and cur_state not in [0]:
			return True
		return False



s = Solution()

while True:
	a = input()
	print(s.isNumber(a))
