#! /usr/bin/env python3
from pprint import pprint
class Solution:
	def isInterleave(self, s1, s2, s3):
		"""
		:type s1: str
		:type s2: str
		:type s3: str
		:rtype: bool
		"""
		if len(s1) == len(s2) == 0:
			return len(s3) == 0
		res = [[False]*len(s2) for _ in range(len(s1))]
		pprint(res)
		res[0][0] = True
		for i in range(len(s1)):
			for j in range(len(s2)):
				if i+j == 0:
					res[i][j] = True
					continue
				k = i + j - 1
				if i > 0 and s1[i - 1] == s3[k]:
					res[i][j] |= res[i-1][j]

				if j > 0 and s2[j - 1] == s3[k]:
					res[i][j] |= res[i][j - 1]
		return res[-1][-1]

s = ["cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc",
	 "abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb",
	 "abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb",
	 ]
s1 =  "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
s = [s1,s2,s3]
a = Solution()
print(a.isInterleave(s[0],s[1],s[2]))
