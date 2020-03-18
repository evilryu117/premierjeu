import pygame
import os
pygame.init()

# genere la fentre de notre jeu

pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((1080,720))

# importer de changer l'arriere plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

running = True

# boucle tant que cette condition est vrai
while running:

    # appliquer l'arrire plan de notre jeu
    screen.blit(background, (0,0))
    # mettre à jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que levenement es fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")