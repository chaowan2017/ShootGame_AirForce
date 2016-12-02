
from button import*
import pygame




class GameCharacters():
    def __init__(self,win):

        self.win = win

        self.__start(win)


    def __start(self, win):

        self.Button_Ice = Button(win, Point(170, 80), 100, 50, "ICE")
        self.Button_Ice.activate()
        self.Button_Fire = Button(win, Point(170, 150), 100, 50, "Fire")
        self.Button_Fire.activate()
        self.Button_Thunder = Button(win, Point(170, 240), 100, 50, "Thunder")
        self.Button_Thunder.activate()
        while 1:
            p=win.getMouse()
            if self.Button_Ice.clicked(p):

                win.close()

                self.speed = 3
                break
            elif self.Button_Fire.clicked(p):

                win.close()

                self.speed = 2

                break
            elif self.Button_Thunder.clicked(p):

                win.close()

                self.speed = 1

                break



if __name__ == "__main__":
    # Creating the screen

     win=GraphWin("AirCraft 2016",340, 300)
     a=GameCharacters(win)