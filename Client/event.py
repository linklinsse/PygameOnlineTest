#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

class EventHandleur:

    def __init__(self, server):
        self.server = server

    def run(self):
        clock = pygame.time.Clock()
        while self.server.running:
            clock.tick(self.server.game_tick)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.server.running = False

if __name__ == "__main__":
    pass
