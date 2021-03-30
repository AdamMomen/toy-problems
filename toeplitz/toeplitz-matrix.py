class Solution:
	def __init__(self, board):
		self.board = board

	def isToeplitz(self):

		rowLimit, colLimit = len(self.board), len(self.board[0])
		matrix = self.board

		for colIdx in range(colLimit - 1):

			startNumber = matrix[0][colIdx]

			for increase in range(min(colLimit - colIdx, colLimit)- 1):
				if  matrix[increase][increase+colIdx] != startNumber:
					return False
					
		for rowIdx in range(colLimit - 1):
			startNumber = matrix[rowIdx][0]
			for increase in range(min(rowLimit - rowIdx, rowLimit) -1):
				if  matrix[rowIdx+increase][increase] != startNumber:
					return False
		return True 

board = [[1,2,3,4],[5,1,2,3],[6,5,0,2]]

print("isToePlitz ", Solution(board=board).isToeplitz())
