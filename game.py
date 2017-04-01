#!/usr/bin/python3

import tkinter as tk
from time import sleep
import Board
from os import system

def drawState():
    for i in range(numCells):
        for j in range(numCells):
            if field.cells[i][j].currentState == 1:
                canv.create_rectangle(
                field.cells[i][j].xCoord * field.cells[i][j].size, field.cells[i][j].yCoord * field.cells[i][j].size, (field.cells[i][j].xCoord + 1) * field.cells[i][j].size,
                (field.cells[i][j].yCoord + 1) * field.cells[i][j].size, fill='blue', outline='black')
            else:
                canv.create_rectangle(
                field.cells[i][j].xCoord * field.cells[i][j].size, field.cells[i][j].yCoord * field.cells[i][j].size, (field.cells[i][j].xCoord + 1) * field.cells[i][j].size,
                (field.cells[i][j].yCoord + 1) * field.cells[i][j].size, fill='white', outline='black')
    sleep(1)
    root.update()

fieldSize = 500
numCells = 25
system('clear')
# запилили окошко
root = tk.Tk()
root.title('Игра "Жизнь" v2.0')
root.geometry(str(fieldSize) + 'x' + str(fieldSize))
canv = tk.Canvas(root, width=fieldSize, height=fieldSize, bg='red')
canv.pack()

# пилим поле с клетками
field = Board.Board(fieldSize, numCells)
field.fillBoard()

while field.isEnd != 0:
    drawState()
    field.nextConfiguration()
print('End!')
root.mainloop()
