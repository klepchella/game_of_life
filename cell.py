#!/usr/bin/python3

class Cell:

    xCoord = None
    yCoord = None
    size = None
    currentState = None
    nextState = None
    neighbors = None

    def __init__(self, boardWidth, i, j, stateCell = 0, cellSize = 10):
        xCoord = i
        yCoord = j
        currentState = stateCell
        size = cellSize

    def numberNeighbor(self):
        neighbors = Board.getNeigh(xCoord, yCoord)

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
