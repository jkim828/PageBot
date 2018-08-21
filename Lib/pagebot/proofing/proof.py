#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------

#     P A G E B O T
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     proof.py
#

class Proof(object):

    leading = 1.2

    def __init__(self, context, **kwargs):
        self.context = context

    def drawGlyphs(self, style, content, size, **kwargs):
        for c in content:
            print(c)