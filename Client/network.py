#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import pygame

from Engine.Entity.idToEntity import IDToEntity

class NetworkHandleur:

    def __init__(self, server):
        self.server = server

    def run(self):
        while self.server.running:
            try:
                self.server.socket.sendto(self.send_to_server().encode(), self.server.server_data)
                data, addr = self.server.socket.recvfrom(65535)

                self.handle_server(data)
            except socket.timeout:
                print("Server do not respond")
                self.server.running = False
            self.server.clock.tick(self.server.game_tick)

    def send_to_server(self):
        ret = ''

        ret += self.encodeActions()
        ret += "LOOK:{},{};".format(self.server.user_mouse_pose[0], self.server.user_mouse_pose[1])

        return ret

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
            tmp = IDToEntity(entity[:4])
            tmp.decode(entity)
            tmp.update()
            if tmp.name == self.server.pseudo:
                self.server.player = tmp
            else:
                self.server.entity_group.add(tmp)


if __name__ == "__main__":
    pass
