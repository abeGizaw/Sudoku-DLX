import sys
import math


class Sudoku:
    def __init__(self, filename):
        self.board_size = 0
        self.partition_size = 0
        self.vals = []
        self.empty_cells = []

        self.read_file(filename)
        self.solve()

    def read_file(self, filename):
        try:
            with open(filename, 'r') as file:
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
        # TODO:  add solve logic here
        solved = self.backtrack_solve()

        if not solved:
            print("No solution found")
            return False
        print("\nOutput\n")
        for row in self.vals:
            print(' '.join(f"{num:3d}" for num in row))
        return True

    def backtrack_solve(self):
        # Todo Implement algorithm here
        self.board_size += 0
        return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sudoku.py <filename>")
        sys.exit(1)
    Sudoku(sys.argv[1])
