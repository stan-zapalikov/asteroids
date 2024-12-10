import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidField = AsteroidField()

    Shot.containers = (shots, updatable, drawable)


    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return

        screen.fill((0,0,0,0))
        
        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            if (obj.colliding(player)):
                sys.exit("Game over !")

        for shot in shots:
            for asteroid in asteroids:
                if (shot.colliding(asteroid)):
                    shot.kill()
                    asteroid.split()


        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()