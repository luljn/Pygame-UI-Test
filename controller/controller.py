import pygame
from model.circle import *
from view.window import *



class Controller :
    
    def __init__(self) :
        
        #Pygame initailization
        pygame.init()
        
        #Game loop variable
        self.running = True
        
        #
        self.window = Window()
        self.circle = Circle(self.window)
    
    #main controller method
    def run(self) :
        
        while self.running :
            
            for event in pygame.event.get() :
                
                if event.type == pygame.QUIT :
                        
                    self.running = False
            
            self.window.show()
            self.circle.move(self.window.dt)
            pygame.display.flip()
        
        self.quit()
    
    def quit(self):
        
        pygame.quit()