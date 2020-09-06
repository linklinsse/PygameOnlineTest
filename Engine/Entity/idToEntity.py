#!/user/bin/env python3
# -*- coding: utf-8 -*-

from Engine.Entity import allEntityId
from Engine.Entity import allEntity

def IDToEntity(entID):
    if entID == allEntityId.PLAYER_ID:
        return allEntity.Player()
    return allEntity.IEntity()

if __name__ == "__main__":
    pass
