import pygame
class Target:

    def __init__(self, mainSurface):
        self.mainSurface = mainSurface
        self.mainSurface.fill((255, 255, 255))
        pygame.init()

    def draw_target(self):
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)
        BLUE = (0, 0, 255)
        BLACK = (0, 0, 0)
        pygame.draw.circle(self.mainSurface, WHITE, (450, 450), 500, 1)
        pygame.draw.circle(self.mainSurface, BLACK, (450, 450), 400, 0)
        pygame.draw.circle(self.mainSurface, BLUE, (450, 450), 300, 0)
        pygame.draw.circle(self.mainSurface, RED, (450, 450), 200, 0)
        pygame.draw.circle(self.mainSurface, YELLOW, (450, 450), 100, 0)

        pygame.display.update()
    def printMouseCoordinates(self, position):
        self.mainSurface.fill((255, 255, 255))
        self.draw_target()
        mousefont = pygame.font.SysFont("Helvetica", 30)
        mouselable = mousefont.render(str(position), 1, (0, 0, 0))
        self.mainSurface.blit(mouselable, (30, 30))
        pygame.display.update()