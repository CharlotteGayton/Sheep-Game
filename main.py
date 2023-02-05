import pygame
from scripts.sheep import SheepChar
from scripts.bucket import BucketChar
from scripts.button import Button
import sys

def main():

    pygame.init()

    sheep = SheepChar()
    bucket = BucketChar()
    startButton = Button()
    
    logo, background = load_assets()

    pygame.display.set_icon(logo)
    pygame.display.set_caption("Sheep Game")

    # Creating our surface
    screen = pygame.display.set_mode((1280,720))

    # Intro Screen
    running = True 
    count = 30
    while running or (count != 0):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN and startButton.rect.collidepoint(pygame.mouse.get_pos()):
                startButton.ifClicked(screen)
                running = False      
        
        screen.blit(background, (0, 0))
        startButton.draw(screen)

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

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit(0)

        screen.blit(background, (0, 0))
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

    background = pygame.image.load("assets/gameBackground.png")

    return logo, background


if __name__=="__main__":
    main()