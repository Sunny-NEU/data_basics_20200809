#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!@Time: 2020/8/11 20:31
#!@Author: Zhang-sl
class Rect:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def intersect(self, rect: 'Rect') -> bool:
        # TODO: implement me
        return not (self.x+self.width <= rect.x or  # left
            self.y+self.height <= rect.y or  # bottom
            self.x >= rect.x+rect.width or  # right
            self.y >= rect.y+rect.height)    # top
