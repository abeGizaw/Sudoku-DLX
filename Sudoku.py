import sys
import math


class Sudoku:
    def __init__(self, filename):
        self.board_size = 0
        self.partition_zie = 0
        self.vals = []

        self.read_file(filename)
        self.solve()

    def read_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.board_size = int(file.readline())
                self.partition_zie = int(math.sqrt(self.board_size))
                print(f'Board size: {self.board_size}x{self.board_size}')

                print("Input:")
                for i, line in enumerate(file):
                    row = list(map(int, line.split()))
                    if len(row) != self.board_size:
                        raise RuntimeError("Incorrect Number of inputs.")
                    print(' '.join(f'{num:3d}' for num in row))
                    self.vals.append(row)

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
