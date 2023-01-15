from tkinter import font
import pygame
from const import *
import time
class Countdown:
    
    def __init__(self) :
        self.total_sec = 0
        '''self.min = int(self.total_sec/60)
        self.sec = self.total_sec - 60*self.min'''
        self.min = 0
        self.sec = 0
        self.total = 0
        self.const = Const()
        self.start = False

    def clock_create(self,surface):
       
        #Sysfont_20 = self.const.font('sys',20)
        pygame.draw.rect(surface,WHITE,(650,235,100,40))
        pygame.draw.rect(surface,WHITE,(610,285,180,20))

        pygame.draw.rect(surface,BLACK,(650,365,100,40))
        pygame.draw.rect(surface,BLACK,(610,415,180,20))
        


    def add_time(self):
        self.total_sec   +=60
        print(self.total_sec)
    def sub_time(self): 
        self.total_sec   -=60 
        print(self.total_sec)

    def count_down(self,surface):
        clock = pygame.time.Clock()
        clock.tick(60)
        
        
        while self.start:
            Arialfont = self.const.font('arial',30)
            self.min = int(self.total_sec/60)
            self.sec = self.total_sec - 60*self.min
            #print(str(self.min)+" : "+ str(self.sec))
            #print(self.start)
            time_now=str(self.min) +":"+ str(self.sec)
            text_time=Arialfont.render(time_now,True,BLACK)
            
        #   create count down rect
            surface.blit(text_time,(650,240))
            self.total_sec-=1
            if self.total_sec==0:
                self.start=False
                #pygame.mixer.Sound.play(sound)
            time.sleep(0.03)
            clock = pygame.time.Clock()
            clock.tick(60)
        

        if self.total_sec < 0:
            self.start=False
            self.total_sec =0
        
    def show_clock(self,surface):
        # show countdown clock to menu screen
        pass

      
        
