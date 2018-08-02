#!/usr/bin/env python3
#-*- coding: utf-8 -*-

arr = [2, 3, 10, 6, 4, 8, 1]

l = []
min_left = 0
max_diff_i = 0
max_diff_j = 0
import pdb
pdb.set_trace()
for i in range(1, len(arr)):
	if arr[i] - arr[min_left] > arr[max_diff_j] - arr[max_diff_i]:
		max_diff_i, max_diff_j = min_left, i
	if arr[min_left] > arr[i]:
		min_left = i

print(arr[max_diff_j], arr[max_diff_i])


