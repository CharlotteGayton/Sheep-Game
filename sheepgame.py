import pygame

def main():

    pygame.init()

    logo, sheep, background, bucket = load_assets()

    pygame.display.set_icon(logo)
    pygame.display.set_caption("Sheep Game")

    # Creating our surface
    screen = pygame.display.set_mode((1280,720))

    #spawning sheep

    running = True

    sheep_x=10
    sheep_y=10

    bucket_x=100
    bucket_y=400

    step=7

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background, (0, 0))
        screen.blit(bucket, (bucket_x, bucket_y))
        screen.blit(sheep, (sheep_x,sheep_y))


        key_input = pygame.key.get_pressed()

        if key_input[pygame.K_LEFT]:
            sheep_x -= step
        if key_input[pygame.K_UP]:
            sheep_y -= step
        if key_input[pygame.K_RIGHT]:
            sheep_x += step
        if key_input[pygame.K_DOWN]:
            sheep_y += step
           
        pygame.display.flip() 
        pygame.display.update()    

        screen.fill((0,0,0))

    
def load_assets():

    # Set my little sheep logo
    logo = pygame.image.load("sheep-closeup-eating-grass.jpg")

    #import sheep 
    sheep = pygame.image.load("Cotswold_Sheep.png")
    sheep = pygame.transform.scale(sheep, (225,300))

    background = pygame.image.load("gameBackground.png")

    bucket = pygame.image.load("bucket-of-water.png")
    bucket = pygame.transform.scale(bucket, (210,210))

    return logo, sheep, background, bucket

if __name__=="__main__":
    main()


