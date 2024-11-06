import pygame
from model.form import Form



class Circle(Form) :
    
    def __init__(self, window, position, color, square, radius = 30) :
        
        super().__init__(window, position)
        self.color = color
        self.square = square
        self.radius = radius
        # self.radius = 30
        # self.position = position
        # self.position = pygame.Vector2(self.window.getScreenWidth() / 2, self.window.getScreenHeight() / 2)
    
    def drawSprite(self) :
        
        pygame.draw.circle(self.window.screen, self.color, self.position, self.radius)
    
    def getRadius(self) :
        
        return self.radius
    
    def move(self) :
        
        self.keys = pygame.key.get_pressed()
        #squares dimensions
        square_width = self.window.getScreenWidth() / 16
        square_height = self.window.getScreenHeight() / 10
        # distance between the center of squares on the same line/column.
        distance = square_width + 10
        #base position circle(the position of the central circle on the square id 4).
        position_x = self.window.getScreenWidth() / 2
        position_y = self.window.getScreenHeight() / 2
        
        if self.keys[pygame.K_UP] : 
            
            if self.square.id == 7 :
                self.position.y = position_y
                self.square.id = 4
                self.square.position.x = (self.window.getScreenWidth() / 2) -  (self.window.getScreenWidth() / 16) / 2
                self.square.position.y = (self.window.getScreenHeight() / 2) - (self.window.getScreenHeight() / 10) /2
        
        if self.keys[pygame.K_DOWN] : 
            
            if self.square.id == 4 :
                self.position.y = position_y + square_width
                self.square.id = 7
                self.square.position.x = (self.window.getScreenWidth() / 2) -  (self.window.getScreenWidth() / 16) / 2
                self.square.position.y =  ((self.window.getScreenHeight() / 2) - (self.window.getScreenHeight() / 10) /2) + ((self.window.getScreenHeight() / 10) + 10)
        
        if self.keys[pygame.K_LEFT] : 
            
            if self.square.id == 7 :
                self.position.x = position_x -  distance
                self.square.id = 6
        
        if self.keys[pygame.K_RIGHT] : 
            
            if self.square.id == 6 :
                self.position.x = position_x
                self.square.id = 7
        
        # dt = self.window.clock.tick(5000) / 100