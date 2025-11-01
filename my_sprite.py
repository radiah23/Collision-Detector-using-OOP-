import pygame

class my_sprite:
    def __init__(self, image_fname: str, loc: tuple[int, int] = (0, 0)):
        if not pygame.get_init():
            pygame.init()
        self.image = pygame.image.load(image_fname)
        self.image_fname = image_fname
        self.loc = loc
        self.width = self.image.get_width()
        self.height = self.image.get_height()
    def __eq__(self,other): 
          
          if other.loc == self.loc and other.width == self.width and other.height== self.height : 
             return True 
          return False 
    
    def get_location(self):
       return self.loc   
    def get_image(self):
      return self.image
    def get_width(self):
      return self.width 
    def get_height(self):
      return self.height 

       
  
      


