#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

class Camera(object):

    def __init__(self, width, height):
        # self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        l, t, _, _ = target.rect # l = left,  t = top
        _, _, w, h = self.state      # w = width, h = height
        self.state = pygame.Rect(-l+w/2, -t+h/2, w, h)
