# Sudoku Solver

## Description
This Sudoku Solver is a Python-based application that utilizes 2 different algorithimgs to solve Sudoku problems.  
SudokuBackTracking.py uses a backtracking algorithm to solve Sudoku puzzles. It's capable of solving 9x9 Sudoku puzzles efficiently 
Sudoku.py incorporates the Dancing Links algorithm (DLX) based on [Donald E. Knuth's paper](https://www.ocf.berkeley.edu/~jchu/publicportal/sudoku/0011047.pdf). With this upgrade, not only has the computation for 9x9 Sudoku puzzles become faster, but it also extends the capability to tackle larger puzzles such as 16x16, 25x25, and 36X36.

## Features
- Reads Sudoku puzzles from a text file.
- Implements both backtracking and DLX for versatile puzzle-solving strategies.
- Efficiently solves 9x9 Sudoku puzzles and scales to handle 16x16, 25x25, and 36X36 puzzles.
- Reads puzzles from a text file and outputs solutions or indicates if no solution exists.  

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
The solver first attempts to use DLX for its efficiency in solving exact cover problems. For 9x9 puzzles, the performance gain is notable, and for larger puzzles, DLX is essential to make the solving process feasible within a reasonable timeframe.

## Personal Note
This is my first project that directly applies a complex data structure from a research paper. Learning and implementing DLX has been a challenging yet rewarding experience, deepening my understanding of algorithmic problem-solving.

## Acknowledgments
- Dancing Links Algorithm devised by [Donald E. Knuth](https://www.ocf.berkeley.edu/~jchu/publicportal/sudoku/0011047.pdf)
- Google Code Archive. [Alex Rudnick's implementation in Python for getting ideas on how to implement some of the methods](https://code.google.com/archive/p/narorumo/wikis/SudokuDLX.wiki)
- [Jonathan Chu's paper](http://www.ocf.berkeley.edu/~jchu/publicportal/sudoku/sudoku.paper.html) for the pseudocode for the Dancing Links implementation
  

