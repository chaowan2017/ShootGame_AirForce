
from button import*
import pygame


SCREEN_DEFAULT_SIZE = (500, 500)

class ScoreList():
    def __init__(self,win):

        self.win = win

      #  self.screen = pygame.display.set_mode(SCREEN_DEFAULT_SIZE, 0, 32)
        self.__start(win)

       # self.fill(0)
       # self.blit( (0, 0, 0), (0, 0))
       # win.setBackground(self,(0, 0, 0))
    def __start(self,win):

        self.Button_Exit=Button(win,Point(170,280),100,50,"Exit")
        self.Button_Exit.activate()



        #self.Caption_Exit=Label(win,Point(170,380),100,50,"Exit")
        item=[]

        f = open("score.txt", "r")
        for i in range(0,5):
            line = f.readline()
            if line:
               line=line.strip()

               p=line.rfind(':')
               len=line.__len__()
               aa= scorestruct(line[p+1:len],line[0:p])
               item.append(aa)
               strpart='%d' %(i+1)
               strshow= strpart+" scores:"+line[0:p]+" name:"+line[p+1:len]
               self.label = Text(Point(160,50+ i*30), strshow)

               self.label.draw(win)



               #self.win.blit(score_text, text_rect)

        f.close()




        while 1:
            p=win.getMouse()
            if self.Button_Exit.clicked(p):
                win.close()
                break



class scorestruct:
   def __init__(self, name, score):
        self.name = name
        self.score = score

if __name__ == "__main__":
    # Creating the screen






    win=GraphWin("ScoreList",340, 420)
    a=ScoreList(win)








   # gm = GameMenu(screen, menu_items)
    # gm.run()



