import pygame 

class Button:

    def __init__(self):
        self.width = 504
        self.height = 192

        self.x_position = 640 - 252
        self.y_position = 540 - 96

        self.image = pygame.image.load("assets/startsign.png")
        self.imageHover = pygame.image.load("assets/startsignhover.png")
        self.currentImage = self.image
        self.scale = (self.width, self.height)

        self.titleHeader = pygame.image.load("assets/newTitle.png")
        # 870 179
        self.titleHeader = pygame.transform.scale(self.titleHeader, (957, 196))
        self.titleHeaderPosX = 161
        #205
        self.titleHeaderPosY = 100


    def ifClicked(self, screen):
        self.x_position += 20
        self.y_position += 10
        self.scale = (self.width - 40, self.height - 20)
        self.draw(screen)
        pygame.mixer.music.load("assets/button-click.wav")
        pygame.mixer.music.play()


    def hover(self):
        self.currentImage = self.imageHover

    def draw(self, screen):
        imageTransformed = pygame.transform.scale(self.currentImage, self.scale)
        screen.blit(imageTransformed, (self.x_position, self.y_position))
        
    def title(self, screen):
        screen.blit(self.titleHeader, (self.titleHeaderPosX, self.titleHeaderPosY))


    @property
    def rect(self):
        return pygame.Rect(self.x_position, self.y_position, self.width, self.height)
