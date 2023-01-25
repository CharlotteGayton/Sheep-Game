import pygame

def main():

    pygame.init()

    logo, sheep = load_assets()

    pygame.display.set_icon(logo)
    pygame.display.set_caption("Sheep Game")

    # Creating our surface
    screen = pygame.display.set_mode((1000,600))

    #spawning sheep

    running = True

    p1=10
    p2=10
    step=5

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.blit(sheep, (p1,p2))

        key_input = pygame.key.get_pressed()

        if key_input[pygame.K_LEFT]:
            p1 -= step
        if key_input[pygame.K_UP]:
            p2 -= step
        if key_input[pygame.K_RIGHT]:
            p1 += step
        if key_input[pygame.K_DOWN]:
            p2 += step
           
        pygame.display.flip() 
        pygame.display.update()    

        screen.fill((0,0,0))

    
def load_assets():

    # Set my little sheep logo
    logo = pygame.image.load("sheep-closeup-eating-grass.jpg")

    #import sheep 
    sheep = pygame.image.load("Cotswold_Sheep.png")

    return logo, sheep

if __name__=="__main__":
    main()


