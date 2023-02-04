import pygame 

class Button:

    def __init__(self):
        self.width = 504
        self.height = 192
        self.image = pygame.image.load("assets/startsign.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.x_position = 640
        self.y_position = 360

    def ifClicked(self):
        self.width = self.width * 0.8
        self.height = self.height * 0.8

    def hover(self, screen):
        darkenedButton = self.image.copy()
        pygame.draw.rect(darkenedButton, (255,0, 0, 0.5),  (self.x_position,self.y_position, self.width,self.height))
        screen.blit(darkenedButton, (self.x_position, self.y_position))


    def draw(self, screen):
        screen.blit(self.image, (self.x_position, self.y_position))
        
    @property
    def rect(self):
        return pygame.Rect(self.x_position, self.y_position, self.height, self.width)
