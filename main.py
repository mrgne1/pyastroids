from asteroid import Asteroid
from player import Player
import pygame
import os
from constants import *

os.environ['SDL_AUDIODRIVER'] = 'dsp'

def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable, drawable = pygame.sprite.Group(), pygame.sprite.Group()

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)

    asteroid = Asteroid(x=SCREEN_WIDTH/4, y=SCREEN_HEIGHT / 4, radius=100)
    updatable.add(asteroid)
    drawable.add(asteroid)
    
    while True:
        screen.fill(color="black")
        for s in updatable:
            s.update(dt=dt)
        for s in drawable:
            s.draw(screen=screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
