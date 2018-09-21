from cell import Cell
import random


#Description:
#   A class that represents a game of minesweeper. Handles all of the major game logic.

class Game:

    #History:
    #   9/20/18: Created and Implemented -Jarod
    #Description:
    #   Creates a new instance of Game.
    #Arguments:
    #   rows: the number of rows/columns in the game.
    #Return:
    #   The new Game Object.
    def __init__(self,rows):
        self.board=[]
        self.flag=False
        for i in range(0,rows):
            for j in range (0,rows):
                self.board.append(Cell(i,j,self.board))
        self.assign_mines(10)
        self.calculate_values()

    #History:
    #   9/20/18: Created and Implemented -Jarod
    #Description:
    #   Assigns the designated number of spaces as mines.
    #Arguments:
    #   count: the number of mines to place in board.
    #Return:
    #   None.
    def assign_mines(self,count):
        while(count>0):
            current=random.randint(0,63)
            if(self.board[current].value!=-1):
                self.board[current].value=-1
                count-=1

    #History:
    #   9/20/18: Created and Implemented -Jarod
    #Description:
    #   Goes through each cell in the board, and assigns it the correct value 
    #       corresponding to the number of mines adjacent to it.
    #Arguments:
    #   None.
    #Return:
    #   None.
    def calculate_values(self):
        for cell in self.board:
            if(cell.value!=-1):
                cell.get_neighbors()
                count=0
                for neighbor in cell.neighbors:
                    if neighbor.value==-1:
                        count+=1;
                cell.value=count
                cell.front=str(cell.value)


    #History:
    #   9/20/18: Created and Implemented -Jarod
    #Description:
    #   Handles the game logic of a mine being clicked.
    #Arguments:
    #   current: the index of the button that was clicked.
    #Return:
    #   None.
    def click(self,current):
        if(self.flag):
            self.board[current].flag()
        else:
            self.board[current].flip()
