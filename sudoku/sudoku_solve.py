import gurobipy as gp
from gurobipy import GRB
import numpy as np
import sys

class SudokuSolve:
    def __init__(self, sudokuMatrix):
        self.sudokuMatrix = sudokuMatrix
        self.model = gp.Model("Sudoku")
        self.model.setParam('OutputFlag', False)
    
    def createVariables(self):
        self.x = [[[self.model.addVar(vtype=GRB.BINARY, name="x_{}_{}_{}".format(i, j, k))
                     for k in range(10)] for j in range(9)]
                        for i in range(9)]
    def cellHasValue(self):
        for i in range(9):
            for j in range(9):
                self.model.addConstr(self.x[i][j][0] == 0)
                k = int(self.sudokuMatrix[i][j])
                if (k != 0):
                    self.model.addConstr(self.x[i][j][k] == 1)

    def oneCellOneValue(self):
        for i in range(9):
            for j in range(9):
                allValues = [self.x[i][j][k] for k in range(1, 10)]
                self.model.addConstr(sum(allValues) == 1)

    def setRow(self):
        for i in range(9):
            for k in range(1, 10):
                allValues = [self.x[i][j][k] for j in range(9)]
                self.model.addConstr(sum(allValues) == 1)

    def setColumn(self):
        for j in range(9):
            for k in range(1, 10):
                allValues = [self.x[i][j][k] for i in range(9)]
                self.model.addConstr(sum(allValues) == 1)

    def setBlock(self):
        for i in range(3):
            for j in range(3):
                for k in range(1, 10):
                    allValues = [self.x[3*i + a][3*j + b][k] 
                                 for a in range(3) for b in range(3)]
                    self.model.addConstr(sum(allValues) == 1)

    def setObjective(self):
        self.model.setObjective(1,  GRB.MINIMIZE)

    def getSolution(self):
        for i in range(9):
            for j in range(9):
                for k in range(1, 10):
                    if self.x[i][j][k].x > 0.5:
                        self.sudokuMatrix[i][j] = k

    def addConstraints(self):
        self.cellHasValue()
        self.oneCellOneValue()
        self.setRow()
        self.setColumn()
        self.setBlock()

    def solve(self):
        self.createVariables()
        self.addConstraints()
        self.setObjective()
        self.model.optimize()
        self.getSolution()

