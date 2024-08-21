import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
import pygame
import os
from constants import *

os.environ['SDL_AUDIODRIVER'] = 'dsp'

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable, drawable = pygame.sprite.Group(), pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    field = AsteroidField()
    
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for s in updatable:
            s.update(dt=dt)

        for s in drawable:
            if s != player and s.has_collided_with(player):
                print("Game over!")
                sys.exit()

        screen.fill(color="black")

        for s in drawable:
            s.draw(screen=screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
