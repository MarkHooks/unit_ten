import pygame
import math


class Target:
    """
    this class is to create a target and keep track of the points
    """
    def __init__(self, mainSurface):

        self.mainSurface = mainSurface
        self.mainSurface.fill((255, 255, 255))
        # this is to set the total points to zero
        self.points = 0
        pygame.init()


    def draw_target(self):
        """
        this draws the target
        :return: none
        """
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


    def add_points(self, position):
        """
        this is to get the points for the target
        :param position: this is to see where on the target they clicked
        :return: none
        """
        self.mainSurface.fill((255, 255, 255))
        self.draw_target()
        mousefont = pygame.font.SysFont("Helvetica", 30)
        x_val = position[0]
        y_val = position[1]
        distance = math.sqrt((x_val - 450) ** 2 + ((y_val - 450) ** 2))

        if distance < 50:
            self.points += 9
        elif distance > 50 and distance < 100:
            self.points += 7
        elif distance > 100 and distance < 150:
            self.points += 5
        elif distance > 150 and distance < 200:
            self.points += 3
        elif distance > 200 and distance < 250:
            self.points += 1

        mouselable = mousefont.render(str(self.points), 1, (0, 0, 0))
        self.mainSurface.blit(mouselable, (30, 30))
        pygame.display.update()
