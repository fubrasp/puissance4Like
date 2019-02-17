#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time

from GameView import *


class Game:
    NUMBER_OF_CHIPS = 42

    def __init__(self):
        self.gamer = 1
        self.playedChips = 0
        self.potentialWinner = False
        self.gameView = GameView()

    def get_gamer(self):
        # Cette fonction retourne le numero du joueur qui doit jouer
        if self.playedChips % 2 == 0:
            gamer_id = 1
        else:
            gamer_id = -1
        return gamer_id

    def display_winner(self):
        if self.gamer == "" or self.gamer is None:
            return "personne n'a gagne"
        else:
            return self.gamer + " a gagne"

    def start(self):
        while self.potentialWinner != "jaune" \
                and self.potentialWinner != "rouge" \
                and self.playedChips < Game.NUMBER_OF_CHIPS:
            time.sleep(0.05)
            # Le joueur joue
            for event in self.gameView.pyGame.event.get():

                self.gameView.gameBoard.display()

                if event.type == self.gameView.pyGame.MOUSEBUTTONUP:
                    x, y = self.gameView.pyGame.mouse.get_pos()
                    gamer = self.get_gamer()
                    colonne = self.gameView.determine_column(x)
                    # On modifie les variables pour tenir compte du jeton depose.
                    self.gameView.gameBoard.put_chip(colonne, gamer)
                    self.playedChips = self.playedChips + 1
                    self.potentialWinner = self.gameView.gameBoard.get_winner()
                    print("GAGNANT ? : " + str(self.potentialWinner))
                    self.gameView.render()
                    self.gameView.pyGame.display.flip()

                if event.type == self.gameView.pyGame.QUIT:
                    sys.exit(0)
