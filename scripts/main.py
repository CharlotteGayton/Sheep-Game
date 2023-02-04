import pygame
from sheep import SheepChar
from bucket import BucketChar

def main():

    pygame.init()

    sheep = SheepChar()
    bucket = BucketChar()
    
    logo, background = load_assets()

    pygame.display.set_icon(logo)
    pygame.display.set_caption("Sheep Game")

    # Creating our surface
    screen = pygame.display.set_mode((1280,720))

    running = True

    bucket_x=100
    bucket_y=400

    step=7

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))
        bucket.draw(screen)
        sheep.draw(screen)

        key_input = pygame.key.get_pressed()
        sheep.move(key_input)

        collide = sheep.rect.colliderect(bucket.rect)
        print(sheep.rect)
        print(bucket.rect)
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