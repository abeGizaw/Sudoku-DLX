import sys
import math


def writeSolutionToFile(filename, sol):
    with open(filename, 'w') as file:
        for row in sol:
            file.write(' '.join(f"{num:3d}" for num in row))
            file.write('\n')


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
                            self.empty_cells.append((i, j))
                    print(' '.join(f'{num:3d}' for num in row))  # Print each number in the row formatted to be 3 digits wide for alignment.
                    self.vals.append(row)  # represents the Sudoku board.

        except FileNotFoundError:
            print(f'Input file not found: {filename}')
            sys.exit(1)

    def solve(self):
        solved = self.backtrack_solve()
        newFileName = self.filename.replace(".txt", "Solution.txt")

        if not solved:
            print("No solution found")
            writeSolutionToFile(newFileName, [[1]])
            return False

        print("\nOutput\n")
        writeSolutionToFile(newFileName, self.vals)
        for row in self.vals:
            print(' '.join(f"{num:3d}" for num in row))
        return True

    def backtrack_solve(self, index = 0):
        if index == len(self.empty_cells):
            return True
        row, col = self.empty_cells[index]
        for val in range(1, self.board_size + 1):
            if self.isValid(val, row, col):
                self.vals[row][col] = val
                if self.backtrack_solve(index + 1):
                    return True
                else:
                    self.vals[row][col] = 0



        return False

    def isValid(self, val, row, col):
        for i in range(self.board_size):
            if self.vals[row][i] == val or self.vals[i][col] == val:
                return False
            if self.sameSquare(val, row, col):
                return False

        return True

    def sameSquare(self, val, row, col):
        rowStart = row - (row % self.partition_size)
        colStart = col - (col % self.partition_size)
        for r in range(rowStart, rowStart + self.partition_size):
            for c in range(colStart, colStart + self.partition_size):
                if self.vals[r][c] == val:
                    return True

        return False
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python Sudoku.py <filename>")
        sys.exit(1)
    Sudoku(sys.argv[1])