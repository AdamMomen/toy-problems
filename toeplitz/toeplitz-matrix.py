class Solution:
	def __init__(self, board):
		self.board = board

	def isToeplitz(self):

		rowLimit, colLimit = len(self.board), len(self.board[0])
		rowIdx, colIdx = 0, 0
		array = self.board
		while rowIdx < rowLimit and colIdx < colLimit:
			if self.isToePlitzDiagonal( rowIdx, 0, pos="row") and self.isToePlitzDiagonal(0, colIdx, pos="col"):
				continue	
			else:
				return False
			rowIdx +=1
			colIdx +=1

		return True 

	def isToePlitzDiagonal(self, row, col, pos ="row"):
		array = self.board
		
		while row < len(array[0]) - 1:
			if array[row][col] != array[row+1][col+1]:
				return False
			col +=1
			row +=1
		return True

board = [[1,2,3,4],[5,1,2,3],[6,5,1,2]]

print("isToePlitz ", Solution(board=board).isToeplitz())
