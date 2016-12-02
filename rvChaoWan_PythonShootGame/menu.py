
from button import*
from ScoreList import *
import pygame

pygame.init()


class GameMenu():
    def __init__(self,win):

        self.win = win
        self.bg_color = (0, 0, 0)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 30)
        self.font_color = (255, 255, 255)
        self.__start(win)
       # self.fill(0)
       # self.blit( (0, 0, 0), (0, 0))

    def __start(self,win):

        self.Button_play=Button(win,Point(170,80),100,50,"Play")
        self.Button_play.activate()

        self.Button_ScoreList=Button(win,Point(170,150),100,50,"ScoreList")
        self.Button_ScoreList.activate()
        self.Button_Exit=Button(win,Point(170,220),100,50,"Exit")
        self.Button_Exit.activate()
        while 1:
            p=win.getMouse()
            if self.Button_play.clicked(p):
                win.close()

                self.operate=1

                break
            elif self.Button_Exit.clicked(p):
                win.close()

                self.operate=0
                ##import mainGame.py
                break
            elif self.Button_ScoreList.clicked(p):
                win2=GraphWin("ScoreList",340, 320)
                win2.setBackground(color_rgb(255,0,0))
                ScoreList(win2)
                ##import mainGame.py




class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

        BackGround = Background('background_image.png', [0, 0])
if __name__ == "__main__":
    # Creating the screen

     win=GraphWin("AirCraft 2016",340, 300)
     a=GameMenu(win)




   # gm = GameMenu(screen, menu_items)
    # gm.run()

