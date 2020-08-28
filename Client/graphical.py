#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

from Engine.Entity.__entity__ import __Entity__

class GraphicalHandleur:

    def __init__(self, server):
        self.server = server

        pygame.init()
        self.screen = pygame.display.set_mode([825, 615])
        pygame.display.set_caption('Game')
        self.myfont = pygame.font.SysFont('Arial', 15)

        self.entity_group = pygame.sprite.Group()
        # self.entity_group.add(__Entity__())

    def run(self):
        clock = pygame.time.Clock()
        while self.server.running:
            clock.tick(self.server.game_tick)

            self.drawScreen()

    def drawScreen(self):
        self.screen.fill((255, 255, 255))
        self.entity_group.draw(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    pass
