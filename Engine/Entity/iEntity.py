#!/user/bin/env python3
# -*- coding: utf-8 -*-

import pygame

from Engine.Entity.allEntityId import IENTITY_ID as ENTITY_ID

class IEntity(pygame.sprite.Sprite):
    """
        Basic entity interface
    """

    def __init__(self, pos_x = 0, pox_y = 0):
        super(IEntity, self).__init__()

        self.image = pygame.Surface([10, 10])
        self.image.fill(pygame.Color(100, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pox_y)

    def encode(self):
        """
            return formated data
        """

        ret = "{}, {}, {}".format(ENTITY_ID, self.rect.center.x, self.rect.center.y)
        return ret

    def decode(self, data):
        """
            accept formated data and set data with it
        """

        data = data.split(',')
        self.rect.center.x = float(data[1])
        self.rect.center.y = float(data[2])

    def update(self):
        """
            will spend one tick in for the entity
        """

        return

if __name__ == "__main__":
    pass
