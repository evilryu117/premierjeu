import pygame

pygame.init()

#cree un seconde class qui va representer notre jeu
class Game:

    def __init__(self):
        # generer notre joueur
        self.player = Player()

# premier class qui va representer notre joueur
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_healh = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
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

    # mettre à jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que levenement es fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
