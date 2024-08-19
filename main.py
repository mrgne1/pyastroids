import pygame
import os
from constants import *

os.environ['SDL_AUDIODRIVER'] = 'dsp'

def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill((0, 0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()
