#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

from Engine.Other.action import EAction

class EventHandleur:

    def __init__(self, server):
        self.server = server
        self.init_key_action()

    def init_key_action(self):
        self.key_action_down = [
            (pygame.K_LEFT,     EAction.MOVE_LEFT_START.value),
            (pygame.K_RIGHT,    EAction.MOVE_RIGHT_START.value),
            (pygame.K_UP,       EAction.MOVE_UP_START.value),
            (pygame.K_DOWN,     EAction.MOVE_DOWN_START.value),
        ]

        self.key_action_up = [
            (pygame.K_LEFT,     EAction.MOVE_LEFT_END.value),
            (pygame.K_RIGHT,    EAction.MOVE_RIGHT_END.value),
            (pygame.K_UP,       EAction.MOVE_UP_END.value),
            (pygame.K_DOWN,     EAction.MOVE_DOWN_END.value),
        ]

    def run(self):
        while self.server.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.server.running = False

                if event.type == pygame.KEYDOWN:
                    for key in self.key_action_down:
                        if event.key == key[0]:
                            self.server.user_action.append(key[1])

                if event.type == pygame.KEYUP:
                    for key in self.key_action_up:
                        if event.key == key[0]:
                            self.server.user_action.append(key[1])

            tmp = pygame.mouse.get_pos()
            if self.server.player:
                self.server.user_mouse_pose = (tmp[0] - 825/2,
                    tmp[1] - 615/2)

            self.server.clock.tick(self.server.game_tick)

if __name__ == "__main__":
    pass
