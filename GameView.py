#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import pygame

from GameBoard import *


class GameView:
    IMAGE_DIRECTORY = "images"

    def __init__(self):
        self.gamer = 1
        self.gameBoard = GameBoard()
        self.pyGame = pygame

        # initialiser l'interface
        # utiliser la librairie pygame
        pygame.init()
        # charger l'image du plateau de jeu
        self.image = pygame.image.load(os.path.join(GameView.IMAGE_DIRECTORY, "plateau.png"))
        # obtenir la taille du plateau de jeu
        taille_plateau_de_jeu = self.image.get_size()
        # stocker cette taille
        self.size = (taille_plateau_de_jeu[0] * 1, taille_plateau_de_jeu[1])
        # setter la taille de la fenetre jeu au meme dimension que celle du plateau de jeu (image)
        self.screen = pygame.display.set_mode(self.size)
        self.screen.blit(self.image, (0, 0))
        pygame.display.flip()

        # charger l'image du pion jaune
        self.yellowChip = pygame.image.load(os.path.join(GameView.IMAGE_DIRECTORY, "pion_jaune.png"))
        # charger l'image du pion rouge
        self.redChip = pygame.image.load(os.path.join(GameView.IMAGE_DIRECTORY, "pion_rouge.png"))
        # Police pour le jeu
        self.font = pygame.font.Font("freesansbold.ttf", 15)

    def determine_column(self, x):
        # Cette fonction retourne la colonne demandee au joueur1
        # Tant que la valeur n'est pas acceptable, on demande la colonne a jouer

        column = x - 16
        column = column / 97
        if column in range(0, 7):
            if self.gameBoard.board[5][int(column)] == 0:
                game_board_state = False
        return int(column)

    def render(self):
        # On nettoye l'ecran de jeu
        self.screen.fill((0, 0, 0))
        # On remet l'image en commencant a la base de l'affichage
        self.screen.blit(self.image, (0, 0))

        # on inverse la gameBoard (backend) pour faciliter les traitements qui suivent
        game_board_game_state = self.gameBoard.reverse_game_board()

        # Affichage de debugging
        self.gameBoard.display()

        # parcours en ordre normal
        for i in range(len(game_board_game_state)):
            for j in range(len(game_board_game_state[i])):
                # cas du joueur jaune
                if game_board_game_state[i][j] == 1:
                    # on place une image d'un pion jaune sur l'écran en fonction de la colonne ou l'on se situe
                    self.screen.blit(self.yellowChip, (16 + 97 * j, 13 - 97.5 * i + 486))
                pygame.display.flip()
                # cas du joueur rouge
                if game_board_game_state[i][j] == -1:
                    # on place une image d'un pion rouge sur l'écran en fonction de la colonne ou l'on se situe
                    self.screen.blit(self.redChip, (16 + 97 * j, 13 - 97.5 * i + 486))
                pygame.display.flip()

