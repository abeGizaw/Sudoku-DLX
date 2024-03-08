import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Sudoku {

    private static int boardSize = 0;
    private static int partitionSize = 0;
    private static int[][] vals = null;
    private static List<int[]> emptyCells = new ArrayList<>();

    public static void main(String[] args){
        String filename = args[0];
        File inputFile = new File(filename);
        Scanner input = null;

        int temp = 0;
        int count = 0;

        try {
            input = new Scanner(inputFile);
            boardSize = input.nextInt();
            partitionSize = (int) Math.sqrt(boardSize);
            System.out.println("Boardsize: " + boardSize + "x" + boardSize);
            vals = new int[boardSize][boardSize];

            System.out.println("Input:");
            int i = 0;
            int j = 0;
            while (input.hasNext()){
                temp = input.nextInt();
                count++;
                System.out.printf("%3d", temp);
                vals[i][j] = temp;
                if (temp == 0) {
                    emptyCells.add(new int[] {i, j});
                }
                j++;
                if (j == boardSize) {
                    j = 0;
                    i++;
                    System.out.println();
                }
                if (j == boardSize) {
                    break;
                }
            }
            input.close();
        } catch (FileNotFoundException exception) {
            System.out.println("Input file not found: " + filename);
        }
        if (count != boardSize*boardSize) throw new RuntimeException("Incorrect number of inputs.");


        boolean solved = solve(0);

        // Output
        if (!solved) {
            System.out.println("No solution found.");
            return;
        }
        System.out.println("\nOutput\n");
        for (int i = 0; i < boardSize; i++) {
            for (int j = 0; j < boardSize; j++) {
                System.out.printf("%3d", vals[i][j]);
            }
            System.out.println();
        }

    }

    public static boolean solve(int index) {
        if (index == emptyCells.size()) {
            return true;
        }

        int[] cell = emptyCells.get(index);
        int row = cell[0];
        int col = cell[1];

        for (int num = 1; num <= boardSize; num++) {
            if (isValid(num, row, col)) {
                vals[row][col] = num;
                if (solve(index + 1)) {
                    return true;
                }
                vals[row][col] = 0; // Backtrack
            }
        }
        return false;
    }

    public static boolean isValid(int val, int row, int col) {
        for (int i = 0; i < boardSize; i++) {
            if (vals[row][i] == val || vals[i][col] == val || sameSquare(val, row, col)) {
                return false;
            }
        }
        return true;
    }

    public static boolean sameSquare(int val, int row, int col) {
        int rowStart = row - row % partitionSize;
        int colStart = col - col % partitionSize;
        for (int r = rowStart; r < rowStart + partitionSize; r++) {
            for (int c = colStart; c < colStart + partitionSize; c++) {
                if (vals[r][c] == val) {
                    return true;
                }
            }
        }
        return false;
    }
}