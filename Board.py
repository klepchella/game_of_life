#!/usr/bin/python3

import Cell
from random import randint

class Board:
# всякие разные поля: размер доски, кол-во клеток на доске, массив под клетки
    boardSize = 0
    numberCells = 0
    cells = []
    isEnd = 0
# заполнили поле начальным состоянием
    def fillBoard(self):
        for i in range(self.numberCells):
            self.cells[i] = []
            for j in range(self.numberCells):
                self.cells[i].append(Cell.Cell(self.numberCells, i, j, randint(0, 2), int(round(self.boardSize / self.numberCells))))

# создали доску
    def __init__(self, bSize = 500, nCells = 10):
        self.boardSize = bSize
        self.numberCells = nCells
        self.cells = [[Cell.Cell] * self.numberCells] * self.numberCells
        self.isEnd = 1

# получили кол-во соседей для клетки
    def getNeigh(self, i, j):
        self.cells[i][j].neighbors = 0

        if self.cells[(i - 1) % self.numberCells][(j - 1) % self.numberCells].currentState != 0:
            self.cells[i][j].neighbors += 1

        if self.cells[(i - 1) % self.numberCells][j].currentState != 0:
            self.cells[i][j].neighbors += 1

        if self.cells[(i - 1) % self.numberCells][(j + 1) % self.numberCells].currentState != 0:
            self.cells[i][j].neighbors += 1

        if self.cells[i][(j - 1) % self.numberCells].currentState != 0:
            self.cells[i][j].neighbors += 1
        if self.cells[i][(j + 1) % self.numberCells].currentState != 0:
            self.cells[i][j].neighbors += 1

        if self.cells[(i + 1) % self.numberCells][(j - 1) % self.numberCells].currentState != 0:
            self.cells[i][j].neighbors += 1

        if self.cells[(i + 1) % self.numberCells][j].currentState != 0:
            self.cells[i][j].neighbors += 1

        if self.cells[(i + 1) % self.numberCells][(j + 1) % self.numberCells].currentState != 0:
            self.cells[i][j].neighbors += 1

# пересчет текущей конфигурации:
# для каждой из ячеек получаем кол-во соседей и в зависимости от него ставим статус
    def nextConfiguration(self):
        self.isEnd = 0
        for string in self.cells:
            for curCell in string:
                self.getNeigh(curCell.xCoord, curCell.yCoord)
                curCell.lifeLaw()   # получили следующий статус клетки
                if curCell.currentState != curCell.nextState: # проверяем, были ли изменения
                    self.isEnd += 1
                curCell.currentState = curCell.nextState
                curCell.nextState = 0
