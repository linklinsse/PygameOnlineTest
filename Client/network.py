#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import pygame

class NetworkHandleur:

    def __init__(self, server):
        self.server = server

    def run(self):
        clock = pygame.time.Clock()
        while self.server.running:
            clock.tick(self.server.game_tick)
            try:
                self.server.socket.sendto('PING'.encode(), self.server.server_data)
                data, addr = self.server.socket.recvfrom(65535)
                self.handle_server(data, addr)
            except socket.timeout:
                print("Server do not respond")
                self.server.running = False

    def handle_server(self, data, addr):
        data = data.decode("utf-8")
        self.server.socket.sendto('Ping'.encode(), self.server.server_data)

if __name__ == "__main__":
    pass
