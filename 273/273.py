#!/usr/bin/env python3
#-*- coding: utf-8 -*-

DEBUG = True
class Solution:
	def numberToWords(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		d_single = {
			"1":"One",
			"2":"Two",
			"3":"Three",
			"4":"Four",
			"5":"Five",
			"6":"Six",
			"7":"Seven",
			"8":"Eight",
			"9":"Nine",
			"0":"Zero"
		}
		d_1x = {
			"10":"Ten",
			"11":"Eleven",
			"12":"Twelve",
			"13":"Thirteen",
			"14":"Fourteen",
			"15":"Fifteen",
			"16":"Sixteen",
			"17":"Seventeen",
			"18":"Eighteen",
			"19":"Nineteen",
		}

		d_x0 = {
			"2" : "Twenty",
			"3" : "Thirty",
			"4" : "Forty",
			"5" : "Fifty",
			"6" : "Sixty",
			"7" : "Seventy",
			"8" : "Eighty",
			"9" : "Ninety",
		}

		def num3_to_words(str_num):
			ret = []
			str_num = str(int(str_num))
			if str_num.__len__() == 3:
				ret.append(d_single[str_num[0]])
				ret.append("Hundred")
			str_num = str(int(str_num[-2:]))
			if str_num.__len__() == 2:
				if str_num[0] == '1':
					ret.append(d_1x[str_num])
				elif str_num[1] == '0':
					ret.append(d_x0[str_num[0]])
				else:
					ret.append(d_x0[str_num[0]])
					ret.append(d_single[str_num[1]])
			if str_num.__len__() == 1 and str_num != "0":
				ret.append(d_single[str_num])
			return ret;

		if num == 0:
			return 'Zero'
		str_num = str(num)
		str_list = []
		while (str_num):
			str_list.insert(0, str_num[-3:])
			str_num = str_num[0:-3]
		if DEBUG:
			print(str_list)
		dummy = ['Billion', 'Million', 'Thousand']
		delimiter = dummy[ -len(str_list) + 1: ] if len(str_list) > 1 else []
		ret_list = []
		for i in str_list:
			tmp = num3_to_words(i)
			if tmp:
				ret_list.extend(tmp)
				if len(delimiter):
					ret_list.append(delimiter[0])
			if len(delimiter):
				delimiter.pop(0)


		ret = " ".join(ret_list)
		if DEBUG:
			print(ret)
		return  ret



s = Solution()
s.numberToWords(123)

