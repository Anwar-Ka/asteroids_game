import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *

def main():
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    our_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

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

if __name__ == "__main__":
    main()