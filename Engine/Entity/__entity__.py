#!/user/bin/env python3
# -*- coding: utf-8 -*-

import pygame

class __Entity__(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([10, 10])
        self.image.fill(pygame.Color(100, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.center = (30, 30)

    def encode(self):
        pass

    def decode(self):
        pass

    def update(self):
        pass

if __name__ == "__main__":
    pass