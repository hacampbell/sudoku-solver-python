# Sudoku Solver
An implementation of a simple AI that makes use of backtracking (a depth first search variant) used to solve a 9x9 sudoku puzzle.

This AI makes use of backtraking, which itself is a varient of depth first search. The program will loop throgh each position in the puzzle grid searching for a number to enter that is valid by the rules of sudoku When a number is found, the value of the position is set to it and the program then moves to the next position. In the event that a dead end is reached, the program backtracks and tries a new value for the position and then continues on until a solution is found. 

Usgae: python3 sudoku.py
