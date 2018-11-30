import pygame, sys
from pygame.locals import*
import target

pygame.init()
mainSurface = pygame.display.set_mode((900, 900), 0, 32)
pygame.display.set_caption("archery")

myTarget = target.Target(mainSurface)
myTarget.draw_target()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            myTarget.printMouseCoordinates(pygame.mouse.get_pos())
