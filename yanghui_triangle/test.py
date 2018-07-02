#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import operator

def y(level):
	def out_put(q, levels):
		levels += 1
		q = q[1:-1]
		q = [str(x) for x in q]
		ws = (levels - len(q))//2
		print("{}{}".format("\t"*ws, "\t".join(q)))
	q = [0, 1, 0]
	out_put(q, level)
	for i in range(level):
		size = len(q)
		prev = 0
		for _ in range(size):
			tmp = q.pop(0)
			new = tmp + prev
			q.append(new)
			prev = tmp
		q.append(0)
		out_put(q, level)

def yy(level):
	q = [1]
	for i in range(level):
		m = [0] + q
		n = q + [0]
		q = list(map(operator.add, m, n))
		print(q)

yy(10)

