#!/usr/bin/python3

import Board

class Cell:

    def __init__(self, boardWidth, i, j, stateCell = 0, cellSize = 10):
        self.xCoord = i
        self.yCoord = j
        self.currentState = stateCell
        self.size = cellSize
        self.neighbors = 0

    def lifeLaw(self):
        if self.neighbors == 2:
            if self.currentState == 1:
                self.nextState = 1
            else:
                self.nextState = 0
        elif self.neighbors == 3:
            self.nextState = 1
        else:
            self.nextState = 0
