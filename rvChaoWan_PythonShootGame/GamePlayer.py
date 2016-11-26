
from button import*
import pygame

pygame.init()


class GamePlayer():
    def __init__(self,win):

        self.win = win

        self.__start(win)
       # self.fill(0)
       # self.blit( (0, 0, 0), (0, 0))
       # win.setBackground(self,(0, 0, 0))
    def __start(self,win):
        self.label = Text(Point(150,50), "input name")
        self.label.draw(win)
        self.Entry_Entry=Entry(Point( 150,80),10)
        self.Entry_Entry.draw(win)


        self.Button_ok=Button(win,Point(150,150),70,50,"OK")
        self.Button_ok.activate()

        while 1:
            p=win.getMouse()
            if self.Button_ok.clicked(p):
                win.close()
                self.namestr=self.Entry_Entry.getText()
                self.returnnum=1


                break





if __name__ == "__main__":
    # Creating the screen

     win=GraphWin("AirCraft 2016",300, 230)
     a=GamePlayer(win)




   # gm = GameMenu(screen, menu_items)
    # gm.run()



