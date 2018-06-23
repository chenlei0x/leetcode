#!/usr/bin/env python3
#-*- coding: utf-8 -*-

d = {
	"I": 1,
	"V": 5,
	"X": 10,
	"L": 50,
	"C": 100,
	"D": 500,
	"M": 1000
}

print(d)

class Solution:
	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		sum = 0
		for i in range(len(s)):
			if i < len(s) - 1 and d[s[i]] < d[s[i+1]]:
				sum -= d[s[i]]
			else:
				sum += d[s[i]]
		print(sum)
		return sum


s = Solution()
s.romanToInt("MCMXCIV")
