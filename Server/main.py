#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import time
from threading import Thread

class Main:

    gameTick = 60

    running = True
    threadPool = []

    def __init__(self, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', port))
        self.sock.settimeout(3)
        print('Init on port:', port)

    def load(self):
        self.threadPool.append(Thread(target=self.network_thread))
        self.threadPool.append(Thread(target=self.command_input_thread))
        self.threadPool.append(Thread(target=self.game_tick_thread))

    def run(self):
        print('Starting Server')

        for thread in self.threadPool:
            thread.start()

        while self.running:
            pass

        for thread in self.threadPool:
            thread.join()

    def network_thread(self):
        while self.running:
            try :
                data, addr = self.sock.recvfrom(65535)
                self.handle_client(data, addr)
            except socket.timeout:
                pass

    def command_input_thread(self):
        while self.running:
            cmd = input('> ').lower()
            if cmd == 'stop':
                print('STOPING SERVER')
                self.running = False
            elif cmd == "help":
                print("[help] to see all commands")
                print("[stop] to stop the server")
            else:
                print('Unknow command, type [help] to see all commands')

    def game_tick_thread(self):
        while self.running:
            time.sleep(1/self.gameTick)

    def handle_client(self, data, addr):
        self.sock.sendto('Data Receved', addr)
        self.sock.sendto(data, addr)

if __name__ == "__main__":
    pass
