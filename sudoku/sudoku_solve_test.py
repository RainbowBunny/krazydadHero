import unittest
import sudoku_solve 
from sudoku_solve import SudokuSolve
import gurobipy as gp
from gurobipy import GRB
import numpy as np

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
    

