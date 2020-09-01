#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import pygame

from Engine.Entity.player import Player

class NetworkHandleur:

    def __init__(self, server):
        self.server = server

    def run(self):
        clock = pygame.time.Clock()
        while self.server.running:
            clock.tick(self.server.game_tick)
            try:
                self.server.socket.sendto(self.encodeActions().encode(), self.server.server_data)
                data, addr = self.server.socket.recvfrom(65535)
                try:
                    self.handle_server(data)
                except:
                    pass
            except socket.timeout:
                print("Server do not respond")
                self.server.running = False

    def encodeActions(self):
        ret = "ACTN:"
        for action in self.server.user_action:
            ret += str(action) + ","
        self.server.user_action = []
        return ret + ";"

    def handle_server(self, data):
        data = data.decode("utf-8")
        data = data.split(';')

        for instruction in data:
            if instruction.startswith("ENTL"):
                self.handle_ENTL(instruction)

    def handle_ENTL(self, data):
        all_entity = data.split(':')[1][1:-2].split('],[')

        self.server.entity_group.empty()

        for entity in all_entity:
            tmp = Player()
            tmp.decode(entity)
            self.server.entity_group.add(tmp)



if __name__ == "__main__":
    pass
