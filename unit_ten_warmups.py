import pygame, sys
from pygame.locals import*

pygame.init()
mainSurface = pygame.display.set_mode((900, 500), 0, 32)
pygame.display.set_caption("SSFS")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()