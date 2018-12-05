# Mark Hooks
# 12/5/18
# this program is to create a target game in pygame
import pygame, sys
from pygame.locals import*
import target

pygame.init()
mainSurface = pygame.display.set_mode((900, 900), 0, 32)
pygame.display.set_caption("archery")

myTarget = target.Target(mainSurface)
myTarget.draw_target()

times = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            myTarget.add_points(pygame.mouse.get_pos())
            times += 1
        if times >= 5:
            MOUSEBUTTONDOWN = 0
