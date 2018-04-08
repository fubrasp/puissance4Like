# -*- coding: utf-8 -*-

liste = [
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

joueur = 1
JetonsJoues = 0
P4 = False


#####################
# Fonctions

def quel_joueur():
    # Cette fonction retourne le numero du joueur qui doit jouer
    if (JetonsJoues % 2 == 0):
        jou = 1
    else:
        jou = 2
    return jou


def choisir_colonne(x, y):
    # Cette fonction retourne la colonne demandee au joueur1
    # Tant que la valeur n'est pas acceptable, on demande la colonne a jouer
    col = x - 16
    col = col / 97
    if col in range(0, 7):
        if (liste[5][col] == 0):
            test = False
    return int(col)


def ligne():
    # Cette fonction retourne la ligne vide correspondant a la colonne demandee
    lig = 0
    for i in range(1, 6):
        if (liste[i][colonne] == 0 and liste[i - 1][colonne] != 0):
            lig = i
    return int(lig)


def verification_P4():
    test2 = False

    # test d'un P4 horizontal
    i = j = 0
    while (not (i == 5 and j == 3)):
        if (liste[i][j] == liste[i][j + 1] and liste[i][j] == liste[i][j + 2] \
                and liste[i][j] == liste[i][j + 3] and liste[i][j] == joueur):
            test2 = True
        if (j == 3):
            i = i + 1
            j = 0
        else:
            j = j + 1

    # test d'un P4 vertical
    i = j = 0
    while (not (i == 2 and j == 6)):
        if (liste[i][j] == liste[i + 1][j] and liste[i][j] == liste[i + 2][j] \
                and liste[i][j] == liste[i + 3][j] and liste[i][j] == joueur):
            test2 = True
        if (j == 6):
            i = i + 1
            j = 0
        else:
            j = j + 1

    # test d'un P4 diagonal vers la droite
    i = j = 0
    while (not (i == 2 and j == 3)):
        if (liste[i][j] == liste[i + 1][j + 1] and liste[i][j] == liste[i + 2][j + 2] \
                and liste[i][j] == liste[i + 3][j + 3] and liste[i][j] == joueur):
            test2 = True
        if (j == 3):
            i = i + 1
            j = 0
        else:
            j = j + 1

    # test d'un P4 diagonal vers la gauche
    i = 0
    j = 3
    while (not (i == 2 and j == 6)):
        if (liste[i][j] == liste[i + 1][j - 1] and liste[i][j] == liste[i + 2][j - 2] \
                and liste[i][j] == liste[i + 3][j - 3] and liste[i][j] == joueur):
            test2 = True
        if (j == 6):
            i = i + 1
            j = 3
        else:
            j = j + 1

    return test2


# -*- coding: cp1252 -*-
import pygame
import sys

pygame.init()
image = pygame.image.load("plateau.png")
sizeim = image.get_size()
size = (sizeim[0] * 1, sizeim[1])
screen = pygame.display.set_mode(size)
screen.blit(image, (0, 0))
pygame.display.flip()


def affichage(matrice):
    screen.fill((0, 0, 0))
    screen.blit(image, (0, 0))
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 1:
                screen.blit(pionrouge, (16 + 97 * j, 13 - 97.5 * i + 486))
            pygame.display.flip()
            if matrice[i][j] == 2:
                screen.blit(pionjaune, (16 + 97 * j, 13 - 97.5 * i + 486))
            pygame.display.flip()


pionjaune = pygame.image.load("pion_jaune.png")
pionrouge = pygame.image.load("pion_rouge.png")
font = pygame.font.Font("freesansbold.ttf", 15)

import time

while (not P4 and JetonsJoues < 42):
    time.sleep(0.1)
    # Le joueur joue
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            joueur = quel_joueur()
            colonne = choisir_colonne(x, y)
            # On modifie les variables pour tenir compte du jeton depose.
            liste[ligne()][colonne] = joueur
            JetonsJoues = JetonsJoues + 1
            P4 = verification_P4()
            affichage(liste)
            pygame.display.flip()

        if event.type == pygame.QUIT:
            sys.exit()