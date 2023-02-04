import pygame
from sheep import SheepChar
from bucket import BucketChar
from button import Button
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
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit(0)
        
        screen.blit(background, (0, 0))
        startButton.draw(screen)

        if pygame.mouse.get_cursor()[0] and startButton.rect.collidepoint(pygame.mouse.get_pos()):
            startButton.hover()

        if pygame.mouse.get_pressed()[0] and startButton.rect.collidepoint(pygame.mouse.get_pos()):
            startButton.ifClicked()
            running = False

        pygame.display.update() 

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