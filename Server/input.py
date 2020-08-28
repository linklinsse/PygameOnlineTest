#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class InputHandleur:

    def __init__(self, server):
        self.server = server

    def run(self):
        while self.server.running:
            cmd = input('> ').lower()
            if cmd == 'stop':
                print('STOPING SERVER')
                self.server.running = False
            elif cmd == "help":
                print("[help] to see all commands")
                print("[stop] to stop the server")
            else:
                print('Unknow command, type [help] to see all commands')

if __name__ == "__main__":
    pass
