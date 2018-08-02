#! /usr/bin/env python3
class Solution:
	def toGoatLatin(self, S):
		"""
		:type S: str
		:rtype: str
		"""
		str_list = S.split()
		ret = []
		acount = 1
		for i in str_list:
			tmp = ""
			if i[0] in "aeiouAEIOU":
				tmp += i + "ma"
			else:
				tmp = i[1:] + i[0]
			tmp += "a"*acount
			ret.append(tmp)
			acount += 1
		return " ".join(ret)

s = Solution()
l = "The quick brown fox jumped over the lazy dog"
ret = s.toGoatLatin(l)
print(ret)

