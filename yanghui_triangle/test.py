#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import operator
import ipdb

def y(level):
	q = [1]
	ipdb.set_trace()
	for i in range(level):
		m = [0] + q
		n = q + [0]
		p = list(map(operator.add, m, n))
		print(p)
		q = p

y(3)


