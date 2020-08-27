#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from Server.main import Main

PORT = 25665

if __name__ == "__main__":
    prog = Main(PORT)
    prog.load()
    prog.run()
