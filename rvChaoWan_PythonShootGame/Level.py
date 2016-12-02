
from button import*
import pygame




class GameLevel():
    def __init__(self,win):

        self.win = win

        self.__start(win)

       # self.fill(0)
       # self.blit( (0, 0, 0), (0, 0))
       # win.setBackground(self,(0, 0, 0))
    def __start(self,win):

        self.Button_normal=Button(win,Point(170,80),100,50,"Normal")
        self.Button_normal.activate()
        self.Button_hard=Button(win,Point(170,150),100,50,"Hard")
        self.Button_hard.activate()
        while 1:
            p=win.getMouse()
            if self.Button_normal.clicked(p):
                win.close()

                self.speed= 3

                break
            elif self.Button_hard.clicked(p):
                win.close()

                self.speed= 1
                ##import mainGame.py
                break




if __name__ == "__main__":
    # Creating the screen

     win=GraphWin("AirCraft 2016",340, 300)
     a=GameLevel(win)




   # gm = GameMenu(screen, menu_items)
    # gm.run()


