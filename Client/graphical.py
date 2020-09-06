#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

from Engine.Entity.player import Player
from Engine.Other.camera import Camera

class GraphicalHandleur:

    def __init__(self, server):
        self.server = server

        pygame.init()
        self.server.screen = pygame.display.set_mode([825, 615])
        pygame.display.set_caption('Game')
        self.myfont = pygame.font.SysFont('Arial', 15)

        self.server.entity_group = pygame.sprite.Group()
        self.server.player = None
        self.camera = Camera(825, 615)

    def run(self):
        while self.server.running:
            self.updateGame()
            self.drawScreen()
            self.server.clock.tick(self.server.game_tick)

    def updateGame(self):
        if self.server.player:
            self.camera.update(self.server.player)

    def drawScreen(self):
        self.server.screen.fill((255, 255, 255))

        for entity in self.server.entity_group:
            self.server.screen.blit(entity.image, self.camera.apply(entity))

        if self.server.player:
            self.server.screen.blit(self.server.player.image, self.camera.apply(self.server.player))

        pygame.display.flip()

if __name__ == "__main__":
    pass
