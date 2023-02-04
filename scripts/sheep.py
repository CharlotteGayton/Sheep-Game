import pygame

class SheepChar:

    def __init__(self):
        self.height = 168
        self.width = 210
        self.image = pygame.image.load("assets/Cotswold_Sheep.png")
        self.image = pygame.transform.scale(self.image, (self.height, self.width))
        self.x_position = 10
        self.y_position = 10
        self.step = 7       
    
    def move(self, key_input):

        if key_input[pygame.K_LEFT]:
            self.x_position -= self.step
        if key_input[pygame.K_UP]:
            self.y_position -= self.step
        if key_input[pygame.K_RIGHT]:
            self.x_position += self.step
        if key_input[pygame.K_DOWN]:
            self.y_position += self.step
    
    def draw(self, screen):
        screen.blit(self.image, (self.x_position, self.y_position))

    @property
    def rect(self):
        return pygame.Rect(self.x_position, self.y_position, self.height, self.width)
