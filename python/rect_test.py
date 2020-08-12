#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!@Time: 2020/8/11 20:32
#!@Author: Zhang-sl
import unittest

from rect import Rect
class RectTest(unittest.TestCase):
    def test_intersect_for_crossing_rects(self):
        self.assertTrue(Rect(1, 1, 1, 1).intersect(Rect(1, 1, 0.5, 0.5)))
        self.assertTrue(Rect(0, 0, 1, 1).intersect(Rect(0.5, 0, 1, 2)))#重叠
        self.assertTrue(Rect(0, 0, 1, 1).intersect(Rect(0, 0, 1, 1)))#完全重合
        self.assertFalse(Rect(0, 0, 1, 1).intersect(Rect(1, 0, 1, 1)))#右边重合
        self.assertFalse(Rect(0, 0, 1, 1).intersect(Rect(0, 1, 1, 1)))#上边重合
        self.assertFalse(Rect(0, 0, 1, 1).intersect(Rect(0, -1, 1, 1)))#下边重合
        self.assertFalse(Rect(0, 0, 1, 1).intersect(Rect(-1, 0, 1, 1)))#左边重合
        self.assertFalse(Rect(0, 0, 1, 1).intersect(Rect(1, 1, 1, 1)))#右上点重合
        self.assertFalse(Rect(0, 0, 1, 1).intersect(Rect(-1, -1, 1, 1)))#右下点重合
        self.assertFalse(Rect(0, 0, 1, 1).intersect(Rect(-1, 1, 1, 1)))#左上点重合
        self.assertFalse(Rect(0, 0, 1, 1).intersect(Rect(-1, -2, 1, 1)))#左下点重合
if __name__ == '__main__':
    unittest.main()