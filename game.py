#!/usr/bin/python3

import Cell
from random import randint

class Board:

# заполнили поле начальным состоянием
    def fillBoard(self):
        for i in range(self.numberCells):
            self.cells[i] = []
            for j in range(self.numberCells):
                self.cells[i].append(Cell.Cell(self.numberCells, i, j, randint(0, 1000) % 2, int(round(self.boardSize / self.numberCells))))

# создали доску
    def __init__(self, bSize = 500, nCells = 10):
        self.boardSize = bSize
        self.numberCells = nCells
        self.cells = [Cell.Cell] * self.numberCells
        for i in range(self.numberCells):
            self.cells[i] = [Cell.Cell] * self.numberCells
        self.isEnd = 1

# получили кол-во соседей для клетки
    def getNeigh(self, i, j):
        self.cells[i][j].neighbors = 0

        for k in range(i - 1, i + 2, 1):
            for l in range(j - 1, j + 2, 1):
                if k != i or l != j:
                    if self.cells[k % self.numberCells][l % self.numberCells].currentState != 0:
                        self.cells[i][j].neighbors += 1

# пересчет текущей конфигурации:
# для каждой из ячеек получаем кол-во соседей и в зависимости от него ставим статус
    def nextConfiguration(self):
        self.isEnd = 0
        for string in self.cells:
            for curCell in string:
                self.getNeigh(curCell.xCoord, curCell.yCoord)
                curCell.lifeLaw()   # получили следующий статус клетки

        for string in self.cells:
            for curCell in string:
                if curCell.currentState != curCell.nextState: # проверяем, были ли изменения
                    self.isEnd += 1
                curCell.currentState = curCell.nextState
                curCell.nextState = 0
