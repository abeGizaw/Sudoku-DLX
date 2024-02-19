# Sudoku Solver

## Description
This Sudoku Solver is a Python-based application that utilizes a backtracking algorithm to solve Sudoku puzzles. It's an AI-powered tool capable of solving 9x9 Sudoku puzzles efficiently 

## Features
- Reads Sudoku puzzles from a text file.
- Solves puzzles using a backtracking algorithm.
- Outputs solutions to text files or indicates if no solution exists.
- Can handle different Sudoku grid sizes (up to 9x9 in the current implementation).

## Input Format
The program expects text files with the following format:

9  
3 6 0 0 2 0 0 8 9  
0 0 0 3 6 1 0 0 0  
0 0 0 0 0 0 0 0 0  
8 0 3 0 0 0 6 0 2  
4 0 0 6 0 3 0 0 7  
6 0 7 0 0 0 1 0 8  
0 0 0 0 0 0 0 0 0  
0 0 0 4 1 8 0 0 0  
9 7 0 0 3 0 0 1 4  


The first line is the size of the Sudoku grid, followed by the grid itself where `0` represents an empty cell.

## Output Format
The solution is output in the same format as the input, with the `0`'s replaced with the correct numbers. If no solution is found, `-1` is written to the output file.

## How It Works
The solver uses a backtracking algorithm, which is a type of depth-first search, to try different number combinations until the solution is found or it's determined that no solution exists.

## Limitations
- Currently optimized for 9x9 Sudoku puzzles. Larger puzzles may require significant computational resources and time.

