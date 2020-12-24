from Grid import Grid
from ActiveShape import ActiveShape
import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

TURQUOISE = (64, 224, 208)  # --> for the I block
YELLOW = (204, 204, 0)      # --> for the O block
BLUE = (65, 105, 225)       # --> for the J block
GREEN = (50, 205, 50)       # --> for the S-block
PURPLE = (75, 0, 130)       # --> for the T-block
RED = (255, 0, 0)           # --> for the Z-block
ORANGE = (255, 140 ,0)      # --> for the L-block
WHITE = (255,255,255)




class Game:
    def __init__(self):
        self.grid = Grid()
        self.activeShape = ActiveShape()
        self.DISPLAY = pygame.display.set_mode((700,800))
        pygame.display.set_caption("Tetris")
        self.DISPLAY.fill(WHITE)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.DISPLAY.fill(WHITE)
            pygame.display.update()
            #clock.tick(FPS)


if __name__ == "__main__":
    tetris = Game()
    tetris.run()
