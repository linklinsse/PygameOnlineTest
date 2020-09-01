#!/user/bin/env python3
# -*- coding: utf-8 -*-

import pygame

from Engine.Entity.iEntity import IEntity

from Engine.Entity.allEntityId import PLAYER_ID as ENTITY_ID

from Engine.Other.action import EAction

class Player(IEntity):
    """
        Basic entity interface
    """

    def __init__(self, pos_x = 0, pox_y = 0, name = "Undefined", user_id = -1):
        super(Player, self).__init__(pos_x, pox_y)

        self.image.fill(pygame.Color(250, 100, 0))
        self.name = name
        self.user_id = user_id

        self.v_x = 0
        self.v_y = 0

        self.initAction()

    def encode(self):
        """
            return formated data
        """

        ret = "{}, {}, {}, {}".format(ENTITY_ID, self.name, self.rect.centerx, self.rect.centery)
        return ret

    def decode(self, data):
        """
            accept formated data and set data with it
        """

        data = data.split(',')
        self.name = str(data[1])
        self.rect.centerx = float(data[2])
        self.rect.centery = float(data[3])

    def update(self):
        """
            will spend one tick in for the entity
        """

        self.rect.move_ip(self.v_x, self.v_y)

    def initAction(self):
        self.fct_tab_acton = [
            (EAction.MOVE_UP_START.value,       lambda self: setattr(self, 'v_y', -5) ),
            (EAction.MOVE_UP_END.value,         lambda self: setattr(self, 'v_y', 0) ),
            (EAction.MOVE_DOWN_START.value,     lambda self: setattr(self, 'v_y', 5) ),
            (EAction.MOVE_DOWN_END.value,       lambda self: setattr(self, 'v_y', 0) ),
            (EAction.MOVE_LEFT_START.value,     lambda self: setattr(self, 'v_x', -5) ),
            (EAction.MOVE_LEFT_END.value,       lambda self: setattr(self, 'v_x', 0) ),
            (EAction.MOVE_RIGHT_START.value,    lambda self: setattr(self, 'v_x', 5) ),
            (EAction.MOVE_RIGHT_END.value,      lambda self: setattr(self, 'v_x', 0) ),
        ]

    def doAction(self, actionList):
        actionList = actionList.split(',')
        for action in actionList:
            if not action:
                continue
            action = int(action)
            for fct_action in self.fct_tab_acton:
                if action == fct_action[0]:
                    fct_action[1](self)
                    break

if __name__ == "__main__":
    pass
