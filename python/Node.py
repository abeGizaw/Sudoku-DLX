import math
from typing import List
import sys

CONSTRAINT_COUNT = 4 # Specific to sudoku
class Node:
    def __init__(self):
        self.left = self
        self.right = self
        self.up = self
        self.down = self
        self.colHead = None

class ColumnNode(Node):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.size = 0
        self.left: ColumnNode = self
        self.right: ColumnNode = self

        # These are for placing values back into the given 2d grid
        self.col = None
        self.row = None
        self.val = None
        sys.setrecursionlimit(1500) # for 36X36 Board 😅


class DancingLinks:
    def __init__(self):
        self.header = ColumnNode("h")
        self.nodes: List[ColumnNode] = []
        self.solution = []
        self.colNames = ['Cell', 'Row', 'Col', 'Grid']
        self.originalBoard = None

    def createEmptyMatrix(self, board, emptyCells):
        self.originalBoard = board
        board_len = len(self.originalBoard)
        print(f'making {4 * len(board)**2} columns')
        lastNode = self.header
        for constraint in range(CONSTRAINT_COUNT):
            nameStart = self.colNames[constraint]
            for section in range(1, board_len+1):
                for val in range(1, len(board[0])+1):
                    # Creating column Node
                    if nameStart != 'Cell':
                        name = f'{nameStart}{section}->{val}'
                    else:
                        name = f'{nameStart}{(section - 1) * board_len + val}'

                    columnNode = ColumnNode(f'{name}')
                    columnNode.row = section
                    columnNode.col = section
                    columnNode.val = val
                    self.nodes.append(columnNode)
                    columnNode.colHead = columnNode

                    # Connecting column Nodes in the matrix
                    columnNode.left = lastNode
                    lastNode.right = columnNode
                    lastNode = columnNode

        # Wrap the head node
        self.header.left = lastNode
        lastNode.right = self.header
        self.fillMatrx(emptyCells)
        self.removeEmptyColumns()

        return
    def fillMatrx(self, emptyCells):
        # Make Nodes in Columns. empty_cell = (row, col, grid)
        for empty_cell in emptyCells:
            for value in range(1, len(self.originalBoard) + 1):
                if self.isValid(value, empty_cell[0] - 1, empty_cell[1] - 1):
                    # Create all the nodes
                    cell_column_index = self.get_column_index('cell', empty_cell[0], empty_cell[1])
                    row_column_index = self.get_column_index('row', empty_cell[0], value)
                    col_column_index = self.get_column_index('col', empty_cell[1], value)
                    grid_column_index = self.get_column_index('grid', empty_cell[2], value)
                    cellNode = Node()
                    cellNode.colHead = self.nodes[cell_column_index]
                    rowNode = Node()
                    rowNode.colHead = self.nodes[row_column_index]
                    colNode = Node()
                    colNode.colHead = self.nodes[col_column_index]
                    gridNode = Node()
                    gridNode.colHead = self.nodes[grid_column_index]

                    # Link these nodes vertically and horizontally
                    self.linkNodes([cellNode, rowNode, colNode, gridNode])



    def get_column_index(self, colType, position, value):
        """
        Calculate the index for a column based on the constraint type, position, and value.
        """
        base_index = {'cell': 0, 'row': 1, 'col': 2, 'grid': 3}[colType] *  len(self.originalBoard)**2
        offset = (position - 1) * len(self.originalBoard) + (value - 1)
        return base_index + offset

    def isValid(self, val, row, col):
        for i in range(len(self.originalBoard)):
            if self.originalBoard[row][i] == val or self.originalBoard[i][col] == val or self.sameSquare(val, row, col):
                return False
        return True
    def sameSquare(self, val, row, col):
        partitionSize = int(math.sqrt(len(self.originalBoard)))
        rowStart = row - (row % partitionSize)
        colStart = col - (col % partitionSize)
        for r in range(rowStart, rowStart + partitionSize):
            for c in range(colStart, colStart + partitionSize):
                if self.originalBoard[r][c] == val:
                    return True
        return False

    def validate_matrix_creation(self):
        """
        This is just a helper making sure every node is connected all 4 ways and every row only has 4 active nodes
        Called for testing purposes
        """
        current = self.header.right
        while current != self.header:
            down_node = current.down
            if current.up.down != current or current.down.up != current or current.left.right != current or current.right.left != current:
                print("PROBLEM", end='')
            while down_node != current:
                if down_node.up.down != down_node or down_node.down.up != down_node or down_node.left.right != down_node or down_node.right.left != down_node:
                    print("PROBLEM",end='')
                rowCount = 1

                while down_node.right.colHead != current:
                    rowCount += 1
                    down_node = down_node.right
                if rowCount != 4:
                    print("Problem")

                down_node = down_node.right
                down_node = down_node.down
            current = current.right

    @staticmethod
    def linkNodes(lisNodes):
        for i in range(len(lisNodes)):
            currNode = lisNodes[i]
            currNode.left = lisNodes[i - 1]

            if i == len(lisNodes) - 1:
                currNode.right = lisNodes[0]
            else:
                currNode.right = lisNodes[i + 1]

            if currNode.colHead.down == currNode.colHead:
                currNode.up = currNode.colHead
                currNode.down = currNode.colHead.down
                currNode.colHead.down = currNode
                currNode.down.up = currNode
            else:
                currNode.up = currNode.colHead.up
                currNode.down = currNode.colHead
                currNode.up.down = currNode
                currNode.down.up = currNode

            currNode.colHead.size += 1

    def search(self, k):
        if self.header.right == self.header:
            # ("Solution found")
            self.processSolution(self.solution)
            # print("Done processing")
            return True

        print("Searching")
        currColumn = self.choose_min_column()
        self.cover(currColumn)
        colNode = currColumn.down
        while colNode != currColumn:
            self.solution.append(colNode)
            parallelNode = colNode.right
            while parallelNode != colNode:
                self.cover(parallelNode.colHead)
                parallelNode = parallelNode.right
            if self.search(k+1):
                return True

            colNode = self.solution.pop()
            parallelNode = colNode.left
            while parallelNode != colNode:
                self.uncover(parallelNode.colHead)
                parallelNode = parallelNode.left

            colNode = colNode.down
        self.uncover(currColumn)
        return False


    @staticmethod
    def cover(columnToCover):
        """
        Note when covering, we go down the column then right of the node
        """
        columnToCover.left.right = columnToCover.right
        columnToCover.right.left = columnToCover.left
        columnNode = columnToCover.down
        while columnNode != columnToCover:
            parallelNode = columnNode.right
            while parallelNode != columnNode:
                parallelNode.up.down = parallelNode.down
                parallelNode.down.up = parallelNode.up
                parallelNode.colHead.size -= 1
                parallelNode = parallelNode.right
            columnNode = columnNode.down


    @staticmethod
    def uncover(columnToUncover):
        """
        Note when uncovering, we go up the column then left of the node
        """
        columnNode = columnToUncover.up
        while columnNode != columnToUncover:
            parallelNode = columnNode.left
            while parallelNode != columnNode:
                parallelNode.colHead.size += 1
                parallelNode.up.down = parallelNode
                parallelNode.down.up = parallelNode
                parallelNode = parallelNode.left
            columnNode = columnNode.up

        columnNode.left.right = columnNode
        columnNode.right.left = columnNode


    def processSolution(self, solution):
        for sol in solution:
            rowInfo = self.findAttributeNode(sol, "Row")
            colInfo = self.findAttributeNode(sol, "Col")

            # Subtract 1 to adjust from 1-indexed to 0-indexed
            row = rowInfo.row - 1
            col = colInfo.col - 1
            value = rowInfo.val # Can be colInfo


            self.originalBoard[row][col] = value

    @staticmethod
    def findAttributeNode(node, attPrefix):
        """
        Finds the node in the linked list that has an attribute starting with 'attribute_prefix'.
        """
        currentNode = node
        while not currentNode.colHead.name.startswith(attPrefix):
            currentNode = currentNode.right
            if currentNode == node:
                raise RuntimeError(f"Could not find column header related to: {attPrefix}")
        return currentNode.colHead


    def choose_min_column(self):
        currentCol = self.header.right
        chosenColumn = currentCol
        while currentCol.right != self.header:
            currentCol = currentCol.right
            if currentCol.size < chosenColumn.size:
                chosenColumn = currentCol
                if chosenColumn.size == 1:
                    return chosenColumn


        return chosenColumn

    def removeEmptyColumns(self):
        for header in self.nodes:
            if header.size == 0:
                header.left.right = header.right
                header.right.left = header.left

