import pygame
from game import Game
pygame.init()



# genere la fentre de notre jeu

pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((1080, 720))

# importer de changer l'arriere plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

# charge notre jeu

game = Game()

running = True

# boucle tant que cette condition est vrai
while running:

    # appliquer l'arrire plan de notre jeu
    screen.blit(background, (0, -200))

    #applique l'image de joueur
    screen.blit(game.player.image , game.player.rect)

    #verifier si le joueur souhaite aller a gouche ou a droite
    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT):
        game.player.move_left()

    print(game.pressed)
    # mettre à jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que levenement es fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
         #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

