import pygame
from scripts.sheep import SheepChar
from scripts.bucket import BucketChar
from scripts.button import Button
from scripts.screen import Screen
import sys

def main():

    pygame.init()

    sheep = SheepChar()
    bucket = BucketChar()
    startButton = Button()
    IntroScreen = Screen('assets\gameBackground.png')
    homeScreen = Screen('assets\gameBackground.png')
    defaultScreenSize = (1280, 720)
    
    logo = load_assets()
    IntroScreen.scale_background(defaultScreenSize)
    # background = pygame.transform.scale(background, (1280, 720))

    pygame.display.set_icon(logo)
    pygame.display.set_caption("Sheep Game")

    # Creating our surface
    screen = pygame.display.set_mode(defaultScreenSize, pygame.RESIZABLE)
    # 1280, 720 -> 256, 144

    # Intro Screen
    running = True 
    count = 30
    screenWidth = 1280
    screenHeight = 720
    while running or (count != 0):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN and startButton.rect.collidepoint(pygame.mouse.get_pos()):
                startButton.ifClicked(screen)
                running = False    
            if event.type == pygame.VIDEORESIZE:
                screenWidth = event.w
                screenHeight = event.w/(1280/720)
                pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)
                IntroScreen.scale_background((screenWidth, screenHeight))
                pygame.display.update() 
        
        screen.blit(IntroScreen.background, (0, 0))
        startButton.draw(screen)
        startButton.title(screen)

        if startButton.rect.collidepoint(pygame.mouse.get_pos()):
            startButton.hover()
        else:
            startButton.currentImage = startButton.image

        pygame.display.update() 
        if not running:
            count -= 1
            if count == 10: 
                startButton.x_position -= 20
                startButton.y_position -= 10
                startButton.scale = (startButton.width, startButton.height)
                homeScreen.scale_background((screenWidth, screenHeight))

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit(0)

        screen.blit(homeScreen.background, (0, 0))
        bucket.draw(screen)
        sheep.draw(screen)

        key_input = pygame.key.get_pressed()
        sheep.move(key_input)

        collide = sheep.rect.colliderect(bucket.rect)
        if collide:
            bucket.empty()

        pygame.display.update() 
    
def load_assets():
    # Set my little sheep logo
    logo = pygame.image.load("assets/sheep-closeup-eating-grass.jpg")

    return logo


if __name__=="__main__":
    main()