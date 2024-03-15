import sys
import math
import os
from Node import DancingLinks




class Sudoku:
    def __init__(self, filename):
        self.board_size = 0
        self.filename = ""
        self.partition_size = 0
        self.vals = []
        self.empty_cells = []
        self.read_file(filename)
        self.solve()

    def read_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.filename = filename
                self.board_size = int(file.readline())
                self.partition_size = int(math.sqrt(self.board_size))
                print(f"Board size: {self.board_size}x{self.board_size}")
                print("Input:")
                for i, line in enumerate(file): # starts after the first line
                    row = list(map(int, line.split())) # Split by whitespace, convert to an integer, and store it in a list
                    if len(row) != self.board_size:
                        raise RuntimeError(f"Incorrect Number of inputs.\n {row}")
                    for j, num in enumerate(row):
                        if num == 0:
                            grid = (i // self.partition_size)*self.partition_size + (j + self.partition_size)//self.partition_size
                            self.empty_cells.append((i + 1, j + 1, grid))


                    print(' '.join(f'{num:3d}' for num in row))  # Print each number in the row formatted to be 3 digits wide for alignment.
                    self.vals.append(row)  # represents the Sudoku board.

        except FileNotFoundError:
            print(f'Input file not found: {filename}')
            sys.exit(1)

    def solve(self):

        dlx = DancingLinks()
        valid = self.validate()
        print(f"IS VALID: {valid}")
        dlx.createEmptyMatrix(self.vals, self.empty_cells)
        solved = dlx.search(0)
        directory = "DLX_Sudoku_Solution"
        new_file_name = self.filename.split('\\')[-1].replace(".txt", "Solution.txt")

        if not solved:
            print("No solution found")
            self.writeSolutionToFile(new_file_name, [[-1]])
            return False

        print("\nOutput\n")
        self.vals = dlx.originalBoard

        # Create directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_path = os.path.join(directory, new_file_name)

        self.writeSolutionToFile(file_path, self.vals)
        for row in self.vals:
            print(' '.join(f"{num:3d}" for num in row))
        return True


    @staticmethod
    def writeSolutionToFile(filename, sol):
        with open(filename, 'w') as file:
            for row in sol:
                file.write(' '.join(f"{num:3d}" for num in row))
                file.write('\n')

    def validate(self):
        for row in range(len(self.vals)):
            for col in range(len(self.vals[0])):
                if self.vals[row][col] != 0 and not self.isValid(self.vals[row][col], row, col):
                    print(f"Saying {self.vals[row][col]} is not valid at {row, col}")
                    return False
        return True

    def isValid(self, val, row, col):
        for i in range(self.board_size):
            if ((self.vals[row][i] == val and i != col) or
                    (self.vals[i][col] == val and i != row) or
                    self.sameSquare(val, row, col)):

                return False
        return True

    def sameSquare(self, val, row, col):
        rowStart = row - (row % self.partition_size)
        colStart = col - (col % self.partition_size)
        for r in range(rowStart, rowStart + self.partition_size):
            for c in range(colStart, colStart + self.partition_size):
                if self.vals[r][c] == val and row != r and col != c is False:
                    return True
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python Sudoku.py <filename>")
        sys.exit(1)
    Sudoku(sys.argv[1])