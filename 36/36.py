#! /usr/bin/env python3

class Solution:
	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		def _is_valid(l):
			d = {}
			for i in l:
				if i == ".":
					continue
				if i in d.keys():
					return False
				d[i] = True
		def get_row(i):
			return  board[i]

		def get_column(i):
			l = []
			for j in board:
				l.append(j[i])
			return l

		def get_box(n):
			l = []
			i = n//3
			j = n%3
			start_i = i*3
			start_j = j*3
			for i in range(start_i, start_i + 3):
				for j in range(start_j, start_j + 3):
					l.append(board[i][j])
			print(l)
			return l

		for i in range(0, 9):
			r = get_row(i)
			if _is_valid(r) == False:
				return False

		for i in range(0, 9):
			r = get_column(i)
			if _is_valid(r) == False:
				return False
		#import ipdb
		#ipdb.set_trace()
		for i in range(0, 9):
			b = get_box(i)
			if _is_valid(b) == False:
				return False

		return True


sudoku = [
	["5","3",".",".","7",".",".",".","."],
	["6",".",".","1","9","5",".",".","."],
	[".","9","8",".",".",".",".","6","."],
	["8",".",".",".","6",".",".",".","3"],
	["4",".",".","8",".","3",".",".","1"],
	["7",".",".",".","2",".",".",".","6"],
	[".","6",".",".",".",".","2","8","."],
	[".",".",".","4","1","9",".",".","5"],
	[".",".",".",".","8",".",".","7","9"]
]
s = Solution();
r = s.isValidSudoku(sudoku)
print(r)

