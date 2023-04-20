from module import *
from sys import exit

pygame.init()

LARGEUR_ECRAN = 1366
HAUTEUR_ECRAN  = 768
DIMENSION_ECRAN = (LARGEUR_ECRAN, HAUTEUR_ECRAN)

ALVEOLE = {"blue" : "alveole_bleue.png", "yellow" : "alveole_jaune.png", "orange" : "alveole_orange.png", "red" : "alveole_rouge.png", "green" : "alveole_verte.png"}
COLOR = ["blue", "green", "yellow", "orange", "red"]


ecran = pygame.display.set_mode(DIMENSION_ECRAN)
horloge = pygame.time.Clock()

en_cours = True

platou = Plateau(3, ecran)

while en_cours:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            exit()
    platou.Afficher()
    pygame.display.update()
    horloge.tick(60)
class Jeu:
    pass
