import pygame

class SheepChar:

    def __init__(self):
        self.height = 150
        self.widthHorizontal = 216
        self.widthVertical = 111
        self.image = pygame.image.load("assets/sheepFront.png")
        self.image = pygame.transform.scale(self.image, (self.widthVertical, self.height))
        self.x_position = 640
        self.y_position = 500
        self.step = 7       
    
    def move(self, key_input):

        if key_input[pygame.K_LEFT]:
            self.x_position -= self.step
            self.image = pygame.image.load("assets/sheepLeft.png")
            self.image = pygame.transform.scale(self.image, (self.widthHorizontal, self.height))
        if key_input[pygame.K_UP]:
            self.y_position -= self.step
            self.image = pygame.image.load("assets/sheepBack.png")
            self.image = pygame.transform.scale(self.image, (self.widthVertical, self.height))
        if key_input[pygame.K_RIGHT]:
            self.x_position += self.step
            self.image = pygame.image.load("assets/sheepRight.png")
            self.image = pygame.transform.scale(self.image, (self.widthHorizontal, self.height))
        if key_input[pygame.K_DOWN]:
            self.y_position += self.step
            self.image = pygame.image.load("assets/sheepFront.png")
            self.image = pygame.transform.scale(self.image, (self.widthVertical, self.height))
    
    def draw(self, screen):
        screen.blit(self.image, (self.x_position, self.y_position))

    @property
    def rect(self):
        return pygame.Rect(self.x_position, self.y_position, self.widthVertical, self.height)
