import random


#PARTIE 1

# Fonction pour difficulté
def choisir_difficulte():
    print("Choisissez la difficulté:")
    print("1. Facile (1 à 5 grenouilles)")
    print("2. Difficile (5 à 10 grenouilles)")
    choix = input("Entrez 1 ou 2 pour choisir la difficulté: ")
    if choix == '1':
        return random.randint(1, 5)  # Facile
    elif choix == '2':
        return random.randint(5, 10)  # Difficile
    else:
        print("Choix non valide. Choisissez 1 ou 2.")
        return choisir_difficulte()  # Demander de nouveau la difficulté

# Initialisation des variables
largeur = 30
hauteur = 25
position_moustique_x = random.randint(0, largeur - 1)
position_moustique_y = random.randint(0, hauteur - 1)
position_maison_x = random.randint(0, largeur - 1)
position_maison_y = random.randint(0, hauteur - 1)
vies = 3
difficulte = choisir_difficulte()

# Fonction pour créer une liste de grenouilles en fonction du niveau de difficulté
def creer_grenouilles(difficulte):
    grenouilles = []
    for _ in range(difficulte):
        x = random.randint(0, largeur - 1)
        y = random.randint(0, hauteur - 1)
        grenouilles.append((x, y))
    return grenouilles

grenouilles = creer_grenouilles(difficulte)

# Fonction pour créer des lacs dans le jeu
def creer_lacs():
    nombre_de_lacs = random.randint(1, 4)
    lacs = []
    for _ in range(nombre_de_lacs):
        x = random.randint(0, largeur - 4)
        y = random.randint(0, hauteur - 4)
        lac = [(x, y), (x, y+1), (x, y+2), (x+1, y), (x+1, y+1), (x+1, y+2), (x+2, y), (x+2, y+1), (x+2, y+2)]
        lacs.extend(lac)
    return lacs

lacs=creer_lacs()

# Fonction pour créer des feux dans le jeu
def creer_feux():
    nombre_de_feux = random.randint(10, 20)
    feux = []
    for _ in range(nombre_de_feux):
        x = random.randint(0, largeur - 1)
        y = random.randint(0, hauteur - 1)
        feux.append((x, y))
    return feux

feux = creer_feux()

#PARTIE 2


# Modifier la fonction pour afficher le plateau
def afficher_plateau():
    for y in range(hauteur):
        for x in range(largeur):
            if x == position_moustique_x and y == position_moustique_y:
                print("\x1b[32m🦟\x1b[0m", end=' ')  # Utiliser \x1b[32m pour la couleur verte
            elif x == position_maison_x and y == position_maison_y:
                print("\x1b[34m🏡\x1b[0m", end=' ')  # Utiliser \x1b[34m pour la couleur bleue
            elif (x, y) in lacs:
                print("\x1b[36m🌊\x1b[0m", end=' ')  # Utiliser \x1b[36m pour la couleur cyan (lacs)
            elif (x, y) in feux:
                print("\x1b[31m🔥\x1b[0m", end=' ')  # Utiliser \x1b[31m pour la couleur rouge (feux)
            else:
                is_grenouille = False
                for grenouille in grenouilles:
                    if x == grenouille[0] and y == grenouille[1]:
                        is_grenouille = True
                        break
                if is_grenouille:
                    print("\x1b[32m🐸\x1b[0m", end=' ')  # Utiliser \x1b[32m pour la couleur verte
                else:
                    print("🌲", end=' ')
        print()
    print("Vies :", "\x1b[31m♥ \x1b[0m" * vies )

# Fonction pour le déplacement de la grenouille
def deplacer_grenouilles():
    for i in range(len(grenouilles)):
        frog_x, frog_y = grenouilles[i]
        if frog_x < position_moustique_x:
            frog_x += 1
        elif frog_x > position_moustique_x:
            frog_x -= 1
        if frog_y < position_moustique_y:
            frog_y += 1
        elif frog_y > position_moustique_y:
            frog_y -= 1
        grenouilles[i] = (frog_x, frog_y)

# Boucle principale du jeu
while vies > 0:
    afficher_plateau()

    # Vérifier si le jeu est terminé
    if position_moustique_x == position_maison_x and position_moustique_y == position_maison_y:
        print("\x1b[33mBravo! Vous avez atteint la maison.\x1b[0m")  # Utiliser \x1b[33m pour la couleur or
        break

    for grenouille in grenouilles:
        if position_moustique_x == grenouille[0] and position_moustique_y == grenouille[1]:
            vies -= 1
            if vies == 0:
                print("\x1b[31mGame Over! La grenouille vous a attrapé.\x1b[0m")  # Utiliser \x1b[31m pour la couleur rouge
                break

    if vies == 0:
        break  # Terminer le jeu si plus de vies

    # Vérifier si le moustique est sur une case de feu
    if (position_moustique_x, position_moustique_y) in feux:
        vies -= 1
        feux.remove((position_moustique_x, position_moustique_y))  # Retirer le feu de la case

    deplacer_grenouilles()  # Les grenouilles suivent le moustique

    deplacement = input("Déplacez le moustique (z/q/s/d): ")
    if deplacement == 'z' and position_moustique_y > 0:
        position_moustique_y -= 1
    elif deplacement == 's' and position_moustique_y < hauteur - 1:
        position_moustique_y += 1
    elif deplacement == 'q' and position_moustique_x > 0:
        position_moustique_x -= 1
    elif deplacement == 'd' and position_moustique_x < largeur - 1:
        position_moustique_x += 1
