import pygame 
import random
from labyrinthe import Labyrinthe
from grid import Grid
from utils import Pos
<<<<<<< HEAD
from apple import Pommes 
=======
from apple import Apple


>>>>>>> 375ef18af66c95cc21c9929e82036287293acbb6

# pygame setup
pygame.init()

# constantes
tilesize = 32  # taille d'une tuile IG
size = (20, 10)  # taille du monde
fps = 30  # fps du jeu
player_speed = 150  # vitesse du joueur
next_move = 0  # tic avant déplacement

# color
color = {
    "ground_color": "#EDDACF",
    "grid_color": "#7F513D",
    "head_color": "#FF0000",
    "body_color": "#00FF00",
    "wall_color": "#000000"
}

level = "data/laby-01.dat"

laby = Labyrinthe(size[0], size[1])
laby.load_from_file(level)
laby.set_color(color["wall_color"])

grid = Grid(size[0], size[1], tilesize)
grid.set_color(color["grid_color"])

screen = pygame.display.set_mode((size[0] * tilesize, size[1] * tilesize))
clock = pygame.time.Clock()
running = True
dt = 0

show_grid = True
show_pos = False

keys = {"UP": 0, "DOWN": 0, "LEFT": 0, "RIGHT": 0}

player_pos = Pos(9, 4)
body_pos = Pos(9, 3)

z_press = 1
s_press = 0
q_press = 0
d_press = 0

pommes = Pommes(screen, laby, tilesize)

# placer les pommes initiales
for _ in range(3):
    pommes.placer_pomme()

# tour de boucle, pour chaque FPS
while running:
    # gestion des I/O
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z or event.key == pygame.K_UP:
                keys['UP'] = 1
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                keys['DOWN'] = 1
            elif event.key == pygame.K_q or event.key == pygame.K_LEFT:
                keys['LEFT'] = 1
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                keys['RIGHT'] = 1
            elif event.key == pygame.K_a:  # Quitter le jeu avec la touche A
                running = False
            elif event.key == pygame.K_p:
                Pause = True
                while Pause:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                            Pause = False
                            # modif après édition
                            fps = 0
                            dt = 999
                            break
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_z or event.key == pygame.K_UP:
                keys['UP'] = 0
                next_move = 1
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                keys['DOWN'] = 0
                next_move = 1
            elif event.key == pygame.K_q or event.key == pygame.K_LEFT:
                keys['LEFT'] = 0
                next_move = 1
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                keys['RIGHT'] = 0
                next_move = 1
            elif event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_g:
                show_grid = not show_grid
            elif event.key == pygame.K_p:
                show_pos = not show_pos
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print("mouse_pos:", pos)

    # gestion des déplacements
    next_move += dt
    if next_move > 0:
        body_pos.x, body_pos.y = player_pos.x, player_pos.y
        new_x, new_y = player_pos.x, player_pos.y
        if keys['UP'] == 1:
            z_press = 1
            s_press = 0
            q_press = 0
            d_press = 0
        elif keys['DOWN'] == 1:
            z_press = 0
            s_press = 1
            q_press = 0
            d_press = 0
        elif keys['LEFT'] == 1:
            z_press = 0
            s_press = 0
            q_press = 1
            d_press = 0
        elif keys['RIGHT'] == 1:
            z_press = 0
            s_press = 0
            q_press = 0
            d_press = 1

        if z_press == 1:
            new_y -= 1
        elif s_press == 1:
            new_y += 1
        elif q_press == 1:
            new_x -= 1
        elif d_press == 1:
            new_x += 1

        # Gérer les bords du labyrinthe de manière circulaire
        new_x %= size[0]
        new_y %= size[1]

        # vérification du déplacement du joueur                                    
        if not laby.hit_box(new_x, new_y):
            player_pos.x, player_pos.y = new_x, new_y
            next_move -= player_speed

    # affichage des différents composants graphiques
    screen.fill(color["ground_color"])

    laby.draw(screen, tilesize)

    if show_grid:
        grid.draw(screen)

    pygame.draw.rect(screen, color["head_color"], pygame.Rect(player_pos.x * tilesize, player_pos.y * tilesize, tilesize, tilesize))
    pygame.draw.rect(screen, color["body_color"], pygame.Rect(body_pos.x * tilesize, body_pos.y * tilesize, tilesize, tilesize * 1))

    # affichage des pommes
    pommes.afficher_pommes()

    # vérification de la collision avec les pommes
    if pommes.ramasser_pomme(player_pos):
        player_speed += 10  # Augmenter la vitesse du joueur lorsqu'il ramasse une pomme
        pommes.placer_pomme()  # Placer une nouvelle pomme après avoir ramassé une pomme

    # vérification de la fin du jeu
    if pommes.check_fin_jeu():
        running = False

    # affichage des modifications du screen_view
    pygame.display.flip()
    # gestion fps
    dt = clock.tick(fps)

# affichage du score à la fin du jeu
pommes.afficher_score()
pygame.quit()
