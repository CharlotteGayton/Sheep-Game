import pygame

class BucketChar:

    def __init__(self):
        self.width = 73
        self.height = 100
        self.image = pygame.image.load("assets/bucket-of-water.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.x_position = 150
        self.y_position = 500
        self.times_slurped = 0       

    def draw(self, screen):
        screen.blit(self.image, (self.x_position, self.y_position))

    def empty(self):
        self.image = pygame.image.load("assets/empty-bucket.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        if self.times_slurped == 0:
            pygame.mixer.Sound.play(pygame.mixer.Sound("assets/slurp-sound.mp3"))
            self.times_slurped += 1

    @property
    def rect(self):
        return pygame.Rect(self.x_position, self.y_position, self.width, self.height)