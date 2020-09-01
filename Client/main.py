#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Thread
import socket
import pygame
from graphical import GraphicalHandleur
from event import EventHandleur
from network import NetworkHandleur

class Main:

    game_tick = 60
    running = True
    thread_pool = []

    def __init__(self, port, ip):
        self.pseudo = input("Your pseudo: ")
        self.server_data = (ip, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(10)

        self.entity_group = pygame.sprite.Group()
        self.user_action = []

        try:
            self.socket.sendto('PING;'.encode(), self.server_data)
            data, addr = self.socket.recvfrom(65535)
            data = data.decode("utf-8")
            if data != "PONG;":
                print("Server did not answer to ping")
                self.running = False
        except socket.timeout:
            print("Server not found")
            self.running = False

    def load(self):
        if not self.running:
            return
        try:
            self.socket.sendto('NEWP:{};'.format(self.pseudo).encode(), self.server_data)
            data, addr = self.socket.recvfrom(65535)
            data = data.decode("utf-8")
            if data != "OKAY;":
                print("Server did not answer to login")
                self.running = False
        except socket.timeout:
            print("Server not answer")
            self.running = False

        self.thread_pool.append(Thread(target=NetworkHandleur(self).run))
        self.thread_pool.append(Thread(target=GraphicalHandleur(self).run))
        self.thread_pool.append(Thread(target=EventHandleur(self).run))

    def run(self):
        if not self.running:
            return

        for thread in self.thread_pool:
            thread.start()

        while self.running:
            pass

        for thread in self.thread_pool:
            thread.join()

if __name__ == "__main__":
    pass
