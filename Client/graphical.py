#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

class GraphicalHandleur:

    def __init__(self, server):
        self.server = server

    def run(self):

        pygame.init()
        self.screen = pygame.display.set_mode([825, 615])
        pygame.display.set_caption('Game')
        # self.myfont = pygame.font.SysFont('Arial', 15)

        clock = pygame.time.Clock()
        while self.server.running:
            clock.tick(self.server.game_tick)

            self.screen.fill((255, 255, 255))
            pygame.display.flip()

if __name__ == "__main__":
    pass
