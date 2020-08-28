#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

class NetworkHandleur:

    def __init__(self, server):
        self.server = server

    def run(self):
        while self.server.running:
            try :
                data, addr = self.server.sock.recvfrom(65535)
                self.handle_client(data, addr)
            except socket.timeout:
                pass

    def handle_client(self, data, addr):
        data = data.decode("utf-8")
        data = data.split(';')
        for action in data:
            if not action:
                return
            if action.startswith("PING"):
                self.server.sock.sendto("PONG;".encode(), addr)
            elif action.startswith("NEWP"):
                self.server.sock.sendto("OKAY;".encode(), addr)
            else:
                self.server.sock.sendto("UNKN;".encode(), addr)

if __name__ == "__main__":
    pass
