import pygame
import math


class Target:

    def __init__(self, mainSurface):
        self.mainSurface = mainSurface
        self.mainSurface.fill((255, 255, 255))
        pygame.init()

    def draw_target(self):
        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)
        BLUE = (0, 0, 255)
        BLACK = (0, 0, 0)
        pygame.draw.circle(self.mainSurface, BLACK, (450, 450), 250, 2)
        pygame.draw.circle(self.mainSurface, BLACK, (450, 450), 200, 0)
        pygame.draw.circle(self.mainSurface, BLUE, (450, 450), 150, 0)
        pygame.draw.circle(self.mainSurface, RED, (450, 450), 100, 0)
        pygame.draw.circle(self.mainSurface, YELLOW, (450, 450), 50, 0)

        pygame.display.update()

    def printMouseCoordinates(self, position):
        self.mainSurface.fill((255, 255, 255))
        self.draw_target()
        mousefont = pygame.font.SysFont("Helvetica", 30)
        x_val = position[0]
        y_val = position[1]
        distance = math.sqrt((x_val - 450) ** 2 + (y_val - 450) ** 2)
        points = 0
        times = 0
        if distance < 50:
            points += 9
            times += 1
        elif distance > 50 < 100:
            points += 7
            times += 1
        elif distance > 100 < 150:
            points += 5
            times += 1
        elif distance > 150 < 200:
            points += 3
            times += 1
        elif distance > 200 < 250:
            points += 1
            times += 1

        mouselable = mousefont.render(str(points), 1, (0, 0, 0))
        self.mainSurface.blit(mouselable, (30, 30))
        pygame.display.update()
