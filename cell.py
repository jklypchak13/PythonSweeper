from PyQt5.QtWidgets import (QWidget, QFrame, QGridLayout,QPushButton,QSizePolicy)
from PyQt5.QtGui import (QColor, QIcon)

class Cell:

    #History:
    #   9/20/18: Created and Implemented -Jarod
    #Description:
    #   Creates a new Cell object.
    #Arguments:
    #   x: the x coordinate of this cell in the game representation.
    #   y: the y coordinate of this cell in the game representation.
    #   board: the array that represents the game board.
    #Return:
    #   The new Cell Object.
    def __init__(self,x,y,board):
        self.row=x
        self.col=y
        self.value=0
        self.board=board
        self.front=""
        self.button=None
        self.flipped=False
        self.flagged=False
    
    #History:
    #   9/20/18: Created and Implemented -Jarod
    #Description:
    #   Sets the current cell's neighbors field to contain and array of all the
    #       cells adjacent to it
    #Arguments:
    #   None.
    #Return:
    #   None.
    def get_neighbors(self):
        result=[];
        for i in range (-1,2):
            for j in range (-1,2):
                current_row=self.row+i
                current_col=self.col+j
                if(current_row>=0 and current_row<8 and current_col>=0 and current_col<8):
                    result.append(self.board[convert_index(current_row,current_col)])
        self.neighbors=result

    #History:
    #   9/20/18: Created and Implemented -Jarod
    #Description:
    #   Sets up the GUI of a button.
    #Arguments:
    #   gui: the QWidget that the current button should be added to.
    #Return:
    #   None.
    def set_button(self,gui):
        self.button=QPushButton(QIcon("")," ",gui.container)
        self.button.setFixedSize(100,100)
        self.flip_side= str(self.value)       
        if(self.value==0):
            self.flip_side=" "
        self.button.clicked.connect(gui.process_click)

    #History:
    #   9/20/18: Created and Implemented -Jarod
    #Description:
    #   Flags or unflags the current cell, based off of its previous state.
    #Arguments:
    #   None.
    #Return:
    #   None.
    def flag(self):
            if self.flagged:
                self.button.setText(" ")
            else:
                self.button.setText("F")
            self.flagged=not self.flagged
            self.button.repaint()

    #History:
    #   9/20/18: Created and Implemented -Jarod
    #Description:
    #   Reveals the current cell, and any adjacent cells if the current cell has a value of 0.
    #Arguments:
    #   None.
    #Return:
    #   None.
    def flip(self):
        if(not self.flipped):
            need_flipped=[]
            need_flipped.append(self)
            while(len(need_flipped)>0):
                current=need_flipped.pop()
                current.button.setText(current.flip_side)
                current.button.repaint()
                current.flipped=True
                current.button.setDisabled(True)
                if(current.value==0):
                    for cell in current.neighbors:
                        if(not cell.flipped):
                            need_flipped.append(cell)


#-----------------------------------HELPER METHODS-------------------------------------------------------
#History:
    #   9/20/18: Created and Implemented -Jarod
    #Description:
    #   Converts the x y coordinates provided to the corresponding index in the array.
    #Arguments:
    #   x: the x coordinate
    #   y: the y coordinate
    #Return:
    #   x*number of rows + y
def convert_index (x,y):
    return (x*8+y)

    