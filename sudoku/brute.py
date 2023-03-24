import gurobipy as gp
from gurobipy import GRB
import numpy as np

model = gp.Model("Sudoku")

x = [1,2,3]
y = x.copy()
y[0] = 4
print(x)
print(y)
