import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (drawable, updatable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()
    
    while True:
        screen.fill("black")
        # Limit to 60fps
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    


if __name__ == "__main__":
    main()
