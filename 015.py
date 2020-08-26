# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 10:29:05 2020

@author: Soaib
"""

""""
The ides is solve the subproblem first and using dynamic programming generate the solution.
"""
# +----+----+---+1
# | 20 | 10 | 4 |
# +----+----+---+1
# | 10 | 6  | 3 |
# +----+----+---+
# | 4  | 3  | 2 |1
# +----+----+---+
# 1    1    1    0


import time

start_time = time.time()

gridSize = 20
grid = [[0 for x in range(gridSize+1)] for y in range(gridSize+1)]

for i in range(gridSize):
    grid[i][gridSize] = 1
    grid[gridSize][i] = 1

for i in range(gridSize-1, -1, -1):
    for j in range(gridSize-1, -1, -1):
        grid[i][j] = grid[i+1][j]+grid[i][j+1]

exe_time = time.time()-start_time

print(grid[0][0])

print(exe_time) # 0 ms


