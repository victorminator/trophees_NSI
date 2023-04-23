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

platou = Plateau1(3, ecran)

while en_cours:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_0:
                platou.add_player_input("0")
            if evenement.key == pygame.K_1:
                platou.add_player_input("1")
            if evenement.key == pygame.K_2:
                platou.add_player_input("2")
            if evenement.key == pygame.K_3:
                platou.add_player_input("3")
            if evenement.key == pygame.K_4:
                platou.add_player_input("4")
            if evenement.key == pygame.K_5:
                platou.add_player_input("5")
            if evenement.key == pygame.K_6:
                platou.add_player_input("6")
            if evenement.key == pygame.K_7:
                platou.add_player_input("7")
            if evenement.key == pygame.K_8:
                platou.add_player_input("8")
            if evenement.key == pygame.K_9:
                platou.add_player_input("9")
    keys = pygame.key.get_pressed()
    platou.draw()
    pygame.display.update()
    horloge.tick(60)
