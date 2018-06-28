#!/usr/bin/env python3
#-*- coding: utf-8 -*-
class Solution:
	def uniqueMorseRepresentations(self, words):
		"""
		:type words: List[str]
		:rtype: int
		"""

		morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

		letters =  [chr(x) for x in range(ord('a'), ord('z') + 1)]

		table = dict(zip(letters, morse))
		#print(table)

		def trans(word):
			ret = ""
			for i in word:
				ret += table[i]
			return ret

		res = set()
		for w in words:
			t = trans(w)
			res.add(t)
		print(res)
		return len(res)


words = ["gin", "zen", "gig", "msg"]
s = Solution()
s.uniqueMorseRepresentations(words)




