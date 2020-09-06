#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import time

from Engine.Entity.player import Player

class NetworkHandleur:
    """
        The network handleur of the server
    """

    def __init__(self, server):
        self.server = server

        self.func_table = [
            ('PING', self.pong, False),
            ('NEWP', self.new_player, False),
            ('ACTN', self.player_action, True),
            ('LOOK', self.player_look, True),
        ]

        self.register_user = []

    def run(self):
        """
            Start the network handleur
        """

        while self.server.running:
            try :
                data, addr = self.server.sock.recvfrom(65535)
                try:
                    self.handle_client(data, addr)
                except Exception as err:
                    self.server.sock.sendto("UNKN;".encode(), addr)
                    print("ERROR:", err, "\n> ")
            except socket.timeout:
                pass

    def handle_client(self, data, addr):
        """
            Handle the data send by the user and transfer it to the corresponding function
        """

        data = data.decode("utf-8")
        data = data.split(';')

        for action in data:
            if not action:
                return

            did_action = False
            for func in self.func_table:
                if action.startswith(func[0]):
                    did_action = True
                    if func[2] and not self.is_login(addr):
                        self.server.sock.sendto("UNLO;".encode(), addr)
                        break
                    func[1](action, addr)

            if not did_action:
                self.server.sock.sendto("UNKN;".encode(), addr)

    def is_login(self, addr):
        """
            Return if the user is already registered or not
        """

        for reg in self.register_user:
            if reg[0] == addr:
                return True
        return False

    def pong(self, data, addr):
        """
            Handling pong function
        """

        self.server.sock.sendto("PONG;".encode(), addr)

    def new_player(self, data, addr):
        """
            Handling the new user function
        """

        pseudo = data.split(':')[1]
        for (reg_addr, reg_name, reg_date) in self.register_user:
            if reg_addr == addr or reg_name == pseudo:
                self.server.sock.sendto("KOKO;".encode(), addr)
                return

        self.register_user.append((addr, pseudo, time.time()))
        self.server.player_list.add(Player(50, 50, pseudo, addr[1]))
        self.server.sock.sendto("OKAY;".encode(), addr)

    def player_action(self, data, addr):
        """
            Handle the player action inside the game
        """

        action = data.split(':')[1]

        for player in self.server.player_list:
            if player.user_id == addr[1]:
                player.doAction(action)
                break

    def player_look(self, data, addr):
        """
            Handle the player action inside the game
        """

        action = data.split(':')[1]

        for player in self.server.player_list:
            if player.user_id == addr[1]:
                player.look(action.split(','))
                break

        self.server.sock.sendto(("ENTL:" + self.encode_all_entity(self.server.player_list) + ";").encode(), addr)

    def encode_all_entity(self, data):
        """
            converte a entity list to a encoded string
        """

        ret = ""
        for entity in data:
            ret += "[" + entity.encode() + "],"
        return ret

if __name__ == "__main__":
    pass
