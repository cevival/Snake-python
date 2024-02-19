import pygame
import random  # Ajout de l'importation du module random

class Pommes:
    def __init__(self, screen, laby, tilesize):
        self.screen = screen
        self.laby = laby
        self.tilesize = tilesize
        self.pommes = []
        self.nb_pommes_ramassees = 0

    def placer_pomme(self):
        width, height = self.laby.getSize()
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        while self.laby.hit_box(x, y):
            x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        self.pommes.append((x, y))

    def afficher_pommes(self):
        for pomme in self.pommes:
            pygame.draw.circle(self.screen, (255, 0, 0), (pomme[0] * self.tilesize + self.tilesize // 2, pomme[1] * self.tilesize + self.tilesize // 2), self.tilesize // 4)

    def ramasser_pomme(self, player_pos):
        for pomme in self.pommes:
            if (player_pos.x, player_pos.y) == pomme:
                self.pommes.remove(pomme)
                self.nb_pommes_ramassees += 1
                return True
        return False

    def check_fin_jeu(self):
        if self.nb_pommes_ramassees >= 5:
            return True
        return False

    def afficher_score(self):
        print("Score:", self.nb_pommes_ramassees)
