import unittest
import sudoku_solve as sudoku_solve 
from sudoku_solve import SudokuSolve
import gurobipy as gp
from gurobipy import GRB
import numpy as np

import os
from input_reader import read_file

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = ' ')
        print()

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
    
    def printMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j], end = ' ')
            print()
    
    def testSample(self, filename, numberOfTest, testingType):
        data = read_file(filename, numberOfTest)

        print(f'Running test from test {testingType}')
        print(f'Number of samples: {numberOfTest}')

        for i in range(numberOfTest):
            print('`````````````````````````````````````````')
            print(f'Test Case no.{i} of {testingType}:')
            print('Sudoku Matrix: ')
            sudokuSolve = SudokuSolve(np.array(data[i]))
            printMatrix(sudokuSolve.sudokuMatrix)
            
            sudokuSolve.solve()
            print(f'Solve time: {int(sudokuSolve.model.RunTime * 1000)} ms')
            print('Sudoku solution: ')
            printMatrix(sudokuSolve.sudokuMatrix)
            print('`````````````````````````````````````````')
            
if __name__ == '__main__':
    solver = TestSudokuSolve()
    solver.testSample('potato.txt', 8, 'Just a potato')
    
    test = ['EZ', 'NO', 'IN', 'CH', 'TF', 'ST', 'IN']
    testSet = ['Easy', 'Novice', 'Intermediate', 'Challenging', 'Tough', 'Super Tough', 'Insane']
    
    directory = 'input_data'
    for name in os.listdir(directory):
        if '.txt' in name:
            for (i, type) in enumerate(test):
                if type in name:
                    solver.testSample(directory + r"/" + name, 8, testSet[i])