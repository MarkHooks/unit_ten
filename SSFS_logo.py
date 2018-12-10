import pygame

class Logo:

    def __init__(self, main_surface):
        self.main_surface = main_surface
        self.GREEN = (0, 102, 71)
        self.GOLD = (255, 209, 63)
        self.WHITE = (255, 255, 255)
        self.main_surface.fill((255, 255, 255))
        pygame.init()

    def draw_logo(self):
        pygame.draw.rect(self.main_surface, self.GREEN, (5, 5, 400, 200), 3)
        pygame.draw.rect(self.main_surface, self.GREEN, (10, 10, 390, 190), 0)
        pygame.draw.polygon(self.main_surface, self.GOLD, ((145, 100), (265, 100), (205, 20)), 3)
        pygame.draw.line(self.main_surface, self.GOLD, (205, 100), (205, 20), 3)
        pygame.draw.line(self.main_surface, self.GOLD, (205, 100), (235, 60), 3)
        pygame.draw.line(self.main_surface, self.GOLD, (205, 100), (175, 60), 3)

        pygame.display.update()

    def draw_words(self):
        school = pygame.font.SysFont("Helvetica", 22)
        lable = school.render("Sandy Spring Friends School", 1, self.WHITE)
        saying = pygame.font.SysFont("Helvetica", 18)
        labl = saying.render("Let Your Lives Speak", 1, self.WHITE)
        self.main_surface.blit(lable, (90, 120))
        self.main_surface.blit(labl, (135, 150))

        pygame.display.update()
