# -----------------------------------------------------------------------------
# FILENAME:			sudoku.py
#
# AUTHOR:			Henry Campbell
#
# DESCRIPTION:		An implementation of backtracking (a depth first search
#					variant) used to solve a 9x9 sudoku puzzle.
#
#                   This AI makes use of backtraking, which itself is a 
#                   varient of depth first search.The program will loop throgh
#                   each position in the puzzle grid searching for a number to
#                   enter that is valid by the rules of sudoku When a number is
#                   found, the value of the position is set to it and the
#                   program then moves to the next position. In the event that
#                   a dead end is reached, the program backtracks and tries a
#                   new value for the position and then continues on until a
#                   solution is found.
#
# USAGE:			python3 sudoku.py
#-----------------------------------------------------------------------------

#!/usr/bin/env python3

class SudokuAgent:
	global sudoku 
	sudoku = [
		[9, 0, 0, 1, 7, 0, 4, 0, 2],
		[1, 6, 0, 0, 4, 0, 0, 9, 5],
		[0, 0, 8, 0, 0, 3, 0, 0, 0],
		[0, 1, 0, 9, 0, 0, 5, 7, 3],
		[0, 4, 0, 0, 0, 0, 0, 2, 0],
		[5, 8, 9, 0, 0, 7, 0, 1, 0],
		[0, 0, 0, 4, 0, 0, 7, 0, 0],
		[6, 7, 0, 0, 2, 0, 0, 5, 8],
		[3, 0, 1, 0, 5, 8, 0, 0, 6]
	]


    # Displays some intro information
	def DisplayHeader (self):
		print("--------------------------------------------------------------")
		print("|                        Sudoku Solver                       |")
		print("--------------------------------------------------------------")
		print("\n")
		print("Author: \t Henry Campbell")
		print("Purpose: \t An AI that solves sudoku puzzles using backtracing")
		print("Parameters: \t None.")

		print("\nThe unsolved puzzle is currently:")
		self.PrettyPrintSudoku()

		input("\nPress enter to begin...")

    # Prints the sudoku puzzle out to the console in a presentable way
	def PrettyPrintSudoku (self):
		for row in sudoku:
			for i in range(len(row)):
				if i == len(row) - 1:
					print(row[i], end = "\n")
				else:
					print(row[i], end = " ")



    # Checks if a given digit is a potential solution for a
	# position by checking that it is not currently present
	# in a given row, column or square.

    # Returns True if a given digit is a potential solution for a
    # position, otherwise False.

    # Parameters:
	#	x: A given row in the sudoku
	#	y: A given column in the sudoku
	#	digit: A digit to check if it's valid in the position
	def IsValidAtPos (self, x, y, digit):
		# Checking on the column
		for i in range(0, 9):
			if sudoku[i][x] == digit:
				return False

		# Checking on the row
		for i in range(0, 9):
			if sudoku[y][i] == digit:
				return False

		# Checking in the square
		x0 = (x // 3) * 3
		y0 = (y // 3) * 3

		for i in range(0, 3): 		# Loops through each row of the square
			for j in range(0, 3): 	# Loops through each column of the row
				if sudoku[y0 + i][x0 + j] == digit:
					return False

		# If we've made it to here, then the digit is valid
		return True


    # Loops through each position of the puzzle and, if the digit is 0,
    # attampts to find a valid solution for it and then recurses. If a
    # dead end is ever reached, the program backtracks and trys a new
    # value.
	def Think (self):
        # Loop through each row and column
		for y in range(9):
			for x in range(9):
				if sudoku[y][x] == 0:
                    # Test values of 1 - 9
					for possibleVal in range (1, 10):
                        # If a potentially correct value is found, set it
						if self.IsValidAtPos(x, y, possibleVal):
							sudoku[y][x] = possibleVal

                            # Notify the user we've places a value
							print(possibleVal, "has been placed at column", x,
                                "row", y)

                            # Recurse in
							self.Think()

							# If we've popped back up to this point it means 
                            # that we've reached a dead end and we need to 
                            # backtrack.
							print("\nA dead end has been reached.", 
                                "Backtracking")

							print("Setting column", x, "row", y, 
                                "( Currently", sudoku[y][x], ") back to 0.\n")

							sudoku[y][x] = 0
					return

		
		# If we've reached this point, we've solved the sudoku.
		print("\n\nA solution to the sudoku has been found. It is:\n")
		self.PrettyPrintSudoku()
		input("\nPress enter to terminate the program.")
		exit()


    # Agent entry point
	def Sudoku (self):
		self.DisplayHeader()
		self.Think()
		

def Main ():
	agent = SudokuAgent()
	agent.Sudoku()


if __name__ == "__main__":
	Main()
