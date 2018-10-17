"""WHATEVER MAN"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import time
sys.path.insert(0,'src/')
from cell import Cell
from game import Game

from PyQt5.QtWidgets import (QWidget, QFrame, QGridLayout,QPushButton,QSizePolicy)
from PyQt5.QtGui import (QColor, QIcon)
from PyQt5.Qt import (QSize,QApplication)

#Main Class for the MatchingGame GUI
class MineSweeper(QWidget):

    #History:
    #   9/20/18: Created and Implemented -Jarod
    #Description:
    #   Initializes the Minesweeper object, setting up the initial GUI
    #Arguments:
    #   None.
    #Return:
    #   The new Minesweeper Object
    def __init__(self):
        super().__init__()
        self.initUI()

    #History:
    #   9/20/18: Created and Implemented -Jarod
    #Description:
    #   Initializes the GUI of Minesweeper
    #Arguments:
    #   None.
    #Return:
    #   None.
    def initUI(self):  
        self.game=Game(8)
        
        self.button_container=QWidget(self)

        
        self.col = QColor(0, 0, 0)      
        self.set_up_buttons(8)
        self.set_up_menu()
        self.set_up_main_window()

#---------------------------------VIEW SETUP----------------------------------------------

    #History:
    #   9/20/18: Created and Implemented -Jarod
    #Description:
    #   Sets up the Button Menu containing the Flag Mode and Reset Buttons
    #Arguments:
    #   None.
    #Return:
    #   None.
    def set_up_menu(self):
        self.flag_button=QPushButton(QIcon(""),"DIGGING",self.button_container)
        self.flag_button.clicked.connect(self.process_flag_click)
        self.reset_button=QPushButton(QIcon(""),"RESET",self.button_container)
        self.reset_button.clicked.connect(self.process_reset_click)
        self.button_grid=QGridLayout(self.button_container)   
        self.button_grid.addWidget(self.flag_button,0,1)
        self.button_grid.addWidget(self.reset_button,0,2)

    #History:
    #   9/20/18: Created and Implemented -Jarod
    #Description:
    #   Organizes the main grid layout of the overall application.
    #Arguments:
    #   None.
    #Return:
    #   None.
    def set_up_main_window(self):
        self.main_grid=QGridLayout(self)
        self.main_grid.addWidget(self.button_container)
        self.main_grid.addWidget(self.container)
        
        #Set Window Title and Show
        self.setFixedSize(1000,1000)
        self.setWindowTitle('MineSweeper')
        self.show()

    #History:
    #   9/20/18: Created and Implemented -Jarod
    #Description:
    #   Initializes Main Boards Buttons, representing the mines and places to dig.
    #Arguments:
    #   rows: the number of rows/columns to be created.
    #Return:
    #   None.
    def set_up_buttons(self,rows):
        self.container=QWidget(self)
        self.container.setFixedSize(100*8,100*8)
        self.mine_grid= QGridLayout(self.container)
        self.mine_grid.setVerticalSpacing(0)
        self.mine_grid.setHorizontalSpacing(0)
        self.buttons=[]
        for i in range(0,rows*rows):
            self.game.board[i].set_button(self)
            self.mine_grid.addWidget(self.game.board[i].button,i/rows,i%rows)

# -------------------------------EVENT HANDLERS------------------------------------------

    #History:
    #   9/20/18: Created and Implemented -Jarod
    #Description:
    #   Processes a click on one of the mine buttons, flagging it or 
    #   digging depending on the state of game.
    #Arguments:
    #   None.
    #Return:
    #   None.
    def process_click(self):

        #Locates the Button that Was Clicked
        button=self.sender()
        current=0
        for i in range (0,64):
            if button==self.game.board[i].button:
                current=i
                
        self.game.click(current)
        

    #History:
    #   9/20/18: Created and Implemented -Jarod
    #Description:
    #   Handles the event that the change mode button is clicked.
    #Arguments:
    #   None.
    #Return:
    #   None.
    def process_flag_click(self):
        if(self.game.flag):
            self.flag_button.setText("DIGGING")
        else:
            self.flag_button.setText("FLAGGING")
        self.game.flag=not self.game.flag

    #History:
    #   9/20/18: Created and Implemented -Jarod
    #Description:
    #   Handles the event that the reset button is clicked, reseting the game.
    #Arguments:
    #   None.
    #Return:
    #   None.
    def process_reset_click(self):
        #TO-DO: Add Reset Functionality
        print()

    

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MineSweeper()
    sys.exit(app.exec_())
