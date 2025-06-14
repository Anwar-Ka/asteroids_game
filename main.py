import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

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
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        pygame.Surface.fill(screen, color = (0,0,0))
        updatable.update(dt)
        
        for asteroid in asteroids:
            if our_player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                exit()

        for shot in shots:
            for asteroid in asteroids:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = fps.tick(60)/1000

if __name__ == "__main__":
    main()