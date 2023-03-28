import unittest
import sudoku_solve as sudoku_solve 
from sudoku_solve import SudokuSolve
import gurobipy as gp
from gurobipy import GRB
import numpy as np

from input_reader import read_file

class TestSudokuSolve(unittest.TestCase):
    def test1(self):
       #create a sudoku problem matrix
        sudokuMatrix = [[1, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        sudokuNumpy = np.array(sudokuMatrix)
        sudokuSolve = SudokuSolve(sudokuNumpy)
        print(sudokuSolve.sudokuMatrix)
        sudokuSolve.solve()
        print(sudokuSolve.sudokuMatrix)
    def testPotato(self, filename, numberOfTest):
        #đọc matrix từ potato
        data = read_file(filename, numberOfTest)
        for i in range(numberOfTest):
            print(f'Test Case no.{i}')
            sudokuNumpy = np.array(data[i])
            sudokuSolve = SudokuSolve(sudokuNumpy)
            print(sudokuSolve.sudokuMatrix)
            sudokuSolve.solve()
            print(sudokuSolve.sudokuMatrix)  
            
if __name__ == '__main__':
    solver = TestSudokuSolve()
    solver.testPotato('potato.txt', 8)