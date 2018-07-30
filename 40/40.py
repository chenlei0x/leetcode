#! /usr/bin/env python3

class Solution:
	def combinationSum2(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		candidates.sort()
		max_elements = target
		def helper(start, end, target, elements):
			if start >= end:
				return []

			if elements > 2:
				ret = []
				for i in range(start, end):
					combines = helper(i + 1, end, target - candidates[i], elements - 1)
					for c in combines:
						c.insert(0, candidates[i])

			if elements == 2:
				ret = []
				i, j = start, end - 1
				while i < j:
					s = candidates[i] + candidates[j]
					if s == target:
						ret.append([candidates[i], candidates[j]])
						i += 1
						j -= 1
					elif s > target:
						j -= 1
					else:
						i += 1

		ret = []
		for e in range(1, max_elements + 1):
			_ret = helper(0, len(candidates), target, e)
			ret.extend(_ret)

		return ret

s = Solution()
print(s.combinationSum2([2,5,2,1,2], 5))
