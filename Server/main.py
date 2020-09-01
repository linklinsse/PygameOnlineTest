#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import socket

from threading import Thread
from input import InputHandleur
from game import GameHandleur
from network import NetworkHandleur

class Main:
    """
        Main class of ther server, he handle the threads
    """

    game_tick = 60

    running = True
    thread_pool = []

    entity_list = pygame.sprite.Group()
    player_list = pygame.sprite.Group()

    def __init__(self, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', port))
        self.sock.settimeout(3)
        print('Init on port:', port)

    def load(self):
        """
            Load all the treads into the thread_pool
        """

        self.thread_pool.append(Thread(target=NetworkHandleur(self).run))
        self.thread_pool.append(Thread(target=InputHandleur(self).run))
        self.thread_pool.append(Thread(target=GameHandleur(self).run))

    def run(self):
        """
            Start all threads then wait the end of running to close all threads
        """

        print('Starting Server')

        for thread in self.thread_pool:
            thread.start()

        while self.running:
            pass

        for thread in self.thread_pool:
            thread.join()

if __name__ == "__main__":
    pass
