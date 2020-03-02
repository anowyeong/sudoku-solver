

#example problem

#board is represented as a set
board = [[3,0,0,8,0,0,0,0,7],
		 [0,9,4,0,6,0,3,0,0],
		 [5,0,0,0,0,1,9,0,0],
		 [0,0,6,0,5,0,0,1,0],
		 [0,0,5,0,2,0,4,0,6],
		 [1,0,3,0,0,7,0,9,0],
		 [7,0,0,4,0,9,5,0,0],
		 [0,4,0,0,7,0,0,0,0],
		 [6,0,0,3,0,0,1,0,0]]


def print_board(board):
	"""
	Description:
	Prints the sudoku board.
	"""
	for i in range(len(board)):

		if (i % 3 == 0 and i != 0):
			print('----------------------------')

		for j in range(len(board[0])):
			if j == 0:
				print(" ", end ="")
			if(j % 3 == 0 and j != 0):
				print(' | ', end="")
			if j == 8:
				print(board[i][j])

			else:
				print(str(board[i][j]) + " ", end="")


def find_empty(board):
	"""
	Description:
	Finds the next empty spot.

	Return:
	The (row, col) coordinates of the empty spot; empty spots are represented as 0.
	"""
	for i in range(9):	# range(len(bo))
		for j in range(9):	# range(len(bo[0]))
			if board[i][j] == 0:
				return (i, j)

	return None


def valid(board, num, pos):
	"""
	Description:
	Checks if the given number follows the sudoku rules
	
	Parameters:
	num = the number to check for
	pos = the position/ coordinates (col, row) of the spot being checked
	
	Returns:
	False if num doesn't follow sudoku rules
	True if it passes
	"""

	# Check row
	for i in range(9):
		if board[pos[0]][i] == num and pos[1] != i:
			return False

	# Check column
	for i in range(9):
		if board[i][pos[1]] == num and pos[0] != i:
			return False

	# Check boxes

	# Use integer division to find the "box" 
	box_x = pos[1] // 3
	box_y = pos[0] // 3

	for i in range(box_y * 3, box_y * 3 + 3):
		for j in range(box_x * 3, box_x * 3 + 3):
			if board[i][j] == num and (i,j) != pos:
				return False

	return True



def solve(board):
	'''
	Description:
	Solves the sudoku board using backtracking/ recurrsion calls

	Returns:
	True if sudoku board is solved
	False if incomplete
	'''

	# base case for backtrack/ recurrsion
	found = find_empty(board)
	if not found:
		return True
	else:
		row, col = found

	
	for i in range(1,10):

		if valid(board, i, (row, col)):

			board[row][col] = i

			if solve(board):
				return True

			# if the board isn't solved, undo the change and 
			# try with another number
			board[row][col] = 0

	return False



print_board(board)
solve(board)
print('\n')
print_board(board)
















