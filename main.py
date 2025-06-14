import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    our_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color = (0,0,0))
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        pygame.display.flip()
        dt = fps.tick(60)/1000
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()