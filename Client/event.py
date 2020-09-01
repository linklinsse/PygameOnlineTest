#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

from Engine.Other.action import EAction

class EventHandleur:

    def __init__(self, server):
        self.server = server

    def run(self):
        clock = pygame.time.Clock()
        while self.server.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.server.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.server.user_action.append(EAction.MOVE_LEFT_START.value)
                    if event.key == pygame.K_RIGHT:
                        self.server.user_action.append(EAction.MOVE_RIGHT_START.value)
                    if event.key == pygame.K_UP:
                        self.server.user_action.append(EAction.MOVE_UP_START.value)
                    if event.key == pygame.K_DOWN:
                        self.server.user_action.append(EAction.MOVE_DOWN_START.value)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.server.user_action.append(EAction.MOVE_LEFT_END.value)
                    if event.key == pygame.K_RIGHT:
                        self.server.user_action.append(EAction.MOVE_RIGHT_END.value)
                    if event.key == pygame.K_UP:
                        self.server.user_action.append(EAction.MOVE_UP_END.value)
                    if event.key == pygame.K_DOWN:
                        self.server.user_action.append(EAction.MOVE_DOWN_END.value)
            clock.tick(self.server.game_tick)

if __name__ == "__main__":
    pass
