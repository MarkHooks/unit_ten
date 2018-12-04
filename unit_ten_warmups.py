import pygame, sys
from pygame.locals import*
import SSFS_logo

pygame.init()
mainSurface = pygame.display.set_mode((500, 250), 0, 32)
pygame.display.set_caption("SSFS")

myTarget = SSFS_logo.Logo(mainSurface)
myTarget.draw_logo()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()