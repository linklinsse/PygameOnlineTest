#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

class GameHandleur:

    def __init__(self, server):
        self.server = server

    def run(self):
        while self.server.running:
            self.server.entity_list.update()
            self.server.player_list.update()
            time.sleep(1/self.server.game_tick)

if __name__ == "__main__":
    pass
