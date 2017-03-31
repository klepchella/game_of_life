#!/usr/bin/python3

import random

class Board:
# всякие разные поля: размер доски, кол-во клеток на доске, массив под клетки
    boardSize = 0
    numberCells = 0
    cells = [[Cell] * numberCells for i in range(numberCells)]

# создали доску
    def __init__(self, bSize = 500, nCells = 10):
        boardSize = bSize
        numberCells = nCells
        fillBoard()

# заполнили поле начальным состоянием
    def fillBoard(self):
        for i in range(numberCells):
            for j in range(numberCells):
                cells[i][j] = Cell(boardSize, i, j, random.randint(0, 10) % 2, int(boardSize / numberCells))

# получили кол-во соседей для клетки
    def getNeigh(self, i, j):
        if cells[(i - 1) % boardSize][(j - 1) % boardSize] != 0:
            cells[i][j].neighbors += 1
        if cells[(i - 1) % boardSize][j % boardSize] != 0:
            cells[i][j].neighbors += 1
        if cells[(i - 1) % boardSize][(j + 1) % boardSize] != 0:
            cells[i][j].neighbors += 1
        if cells[i % boardSize][(j - 1) % boardSize] != 0:
            cells[i][j].neighbors += 1
        if cells[i % boardSize][(j + 1) % boardSize] != 0:
            cells[i][j].neighbors += 1
        if cells[(i + 1) % boardSize][(j - 1) % boardSize] != 0:
            cells[i][j].neighbors += 1
        if cells[i % boardSize][(j - 1) % boardSize] != 0:
            cells[i][j].neighbors += 1
        if cells[(i + 1) % boardSize][(j + 1) % boardSize] != 0:
            cells[i][j].neighbors += 1

# пересчет текущей конфигурации:
# для каждой из ячеек получаем кол-во соседей и в зависимости от него ставим статус
    def nextConfiguration(self):
        for string in cells:
            for curCell in string:
                curCell.numberNeighbor()    # посчитали кол-во соседей
                curCell.lifeLaw()   # получили следующий статус клетки
                curCell.currentState = curCell.nextState
                curCell.nextState = None
