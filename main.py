#Cellular Automata
import random
from turtle import *

class CellBoard:

    # Creates initial board
    # x, y creates length and height
    # alive chance is a float between 0 and 1
    def __init__ (self, x, y, aliveChance, alive, dead, fileToOpen):
        
        # Predefine variables
        self.board = []
        self.prev_board = []
        self.steps = 0
        self.alive = alive
        self.dead = dead

        # If given a string:
        # Try to open a file
        if (fileToOpen != ""):

            try:
                f = open(fileToOpen,'r')
                for line in f:
                    line = line.replace("\n","")
                    self.board.append(line)
                    self.prev_board.append(line)
                f.close()
            except error as e:
                print("An error occored. It has been printed below.")
                print(e.value)
        # Else generate a random board
        else:
            for yi in range(0,y):
                self.board.append("")
                self.prev_board.append("")
                
                for xi in range(0,x):
                    if random.random() <= aliveChance:
                        self.board[yi] += "1"
                        self.prev_board[yi] += "1"
                    else:
                        self.board[yi] += "0"
                        self.prev_board[yi] += "0"
            

    def step(self):
        self.steps += 1

        #loop through each cell
        for yi in range(0,len(self.prev_board)):
            self.board[yi] = ""
            for xi in range(0,len(self.prev_board[0])):
                
                count = 0
                # neighbour y index and neight x index
                for  nyi in range(-1,2):
                    
                    for nxi in range(-1,2):

                        #if not checking self
                        if nyi != 0 or nxi != 0:
                            

                            #Wrap around board
                            if nyi+yi == len(self.prev_board):
                                nyi = -yi
                            if nxi+xi == len(self.prev_board[0]):
                                nxi = -xi

                            #Add to neightbour count
                            if self.prev_board[nyi+yi][nxi+xi] == "1":
                                count += 1

                if count == 3 or (count == 2 and self.prev_board[yi][xi] == "1"):
                    self.board[yi]  += "1"
                else:
                    self.board[yi] += "0"

        for yi in range(0,len(self.prev_board)):
            self.prev_board[yi] = self.board[yi]

    def __str__ (self):
        printableString = ''
        for yi in range(len(self.board)-1,-1,-1):
            printableString += self.board[yi] + "\n"

        printableString = printableString.replace("1", self.alive).replace("0",self.dead)
        printableString += "Steps: " + str(self.steps)
        return str(printableString)


import time
import os

# Variables just to change screen size, and number of cells on x and h axis
length = 800
height = 500
cell_size = 10
#


game = CellBoard(
    round(length / cell_size),
    round(height /cell_size),
    0.45, "O", " ", input("Pattern: ")
)


setup(length, height)

pu()
speed('fastest')

while 1==1:
    
    tracer(0,0)
    clear()
    pu()
    for yi in range(len(game.board)-1):
            for xi in range(len(game.board[0])-1):
                if game.board[yi][xi] == '1':
                    goto(
                        -length / 2 + cell_size * xi,
                        -height / 2 + cell_size * yi
                    )
                    
                    dot(cell_size)
    update()
    game.step()
    #time.sleep(0.05)
    
    
