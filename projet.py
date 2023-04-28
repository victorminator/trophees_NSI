from module import *
from sys import exit


horloge = pygame.time.Clock()

en_cours = True

platou = Plateau1(3)
platou.activate()
while en_cours:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evenement.type == pygame.KEYDOWN:
            for i in range(10):
                if evenement.key == eval("pygame.K_" + str(i)): # Simplifié
                    platou.add_player_input(str(i))
    keys = pygame.key.get_pressed()
    platou.main_function()
    pygame.display.update()
    horloge.tick(60)