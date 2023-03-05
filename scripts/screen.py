import pygame

class Screen:

    def __init__(self, path_to_screen_image):
        self.background = pygame.image.load(path_to_screen_image)
        self.background = pygame.transform.scale(self.background, (1280, 720))

    def scale_background(self, size):
        self.background = pygame.transform.scale(self.background, size)

