#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

from Engine.Entity.player import Player

class GraphicalHandleur:

    def __init__(self, server):
        self.server = server

        pygame.init()
        self.server.screen = pygame.display.set_mode([825, 615])
        pygame.display.set_caption('Game')
        self.myfont = pygame.font.SysFont('Arial', 15)

        self.server.entity_group = pygame.sprite.Group()

    def run(self):
        clock = pygame.time.Clock()
        while self.server.running:
            self.drawScreen()
            clock.tick(self.server.game_tick)

    def drawScreen(self):
        self.server.screen.fill((255, 255, 255))
        self.server.entity_group.draw(self.server.screen)
        pygame.display.flip()

if __name__ == "__main__":
    pass
