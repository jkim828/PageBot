#!/usr/bin/evn python
# encoding: utf-8
# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     TextBaselines.py
#
#     Show how alignment of baselines work for 
from __future__ import print_function

from pagebot.document import Document
from pagebot.constants import GRID_LINE, GRID_COL, GRID_SQR, GRID_ROW
from pagebot.toolbox.units import p, fr, pt
from pagebot.toolbox.color import color
from pagebot.composer import Composer
from pagebot.conditions import *

COL = p(16) # Column width
GUTTER = p(2) # Gutter width
COLS = 5 # Number of columns
PADDING = p(5) # Padding of the page
LEADING = pt(18)

# Calculate the width of the page from the column measures
W = COLS * COL + (COLS-1) * GUTTER + 2*PADDING
H = 1000 # Fixed height

GRIDX = [] # Construct the column grid measures
for n in range(COLS-1):
    GRIDX.append((COL, GUTTER))
GRIDX.append((COL, p(0))) # Last column does not have gutter

h1Style = dict(fontSize=18, textFill=(1, 0, 0))
pStyle = dict(fontSize=10)
styles = dict(h1Style=h1Style, pStyle=pStyle)

# Create a document with these attributes, single page.
doc = Document(w=W, h=H, padding=PADDING, gridX=GRIDX, originTop=False, styles=styles,
    baselineGrid=LEADING)
view = doc.view
view.showBaselineGrid = [GRID_LINE] # Set the view to show the baseline grid
view.showGrid = [GRID_COL, GRID_ROW, GRID_SQR] # Set the view to display the grid

s = """

# What is PageBot?

PageBot is a page layout program that enables designers to create high quality documents using code. It is available both as Python library working with [DrawBot](http://www.drawbot.com) and as part of a collection of stand-alone desktop applications that can be created from it. Other contexts such as [Flat](http://xxyxyz.org/flat) (currently under development) allow PageBot to run environments other Mac OS X, for example on web servers. Initiated by [Type Network](https://typenetwork.com), the aim is to create a system for scriptable applications generating professionally designed documents that use high quality typography.

* The core library, tutorial and basic examples for PageBot are available under
MIT Open Source license from [github.com/TypeNetwork/PageBot](https://github.com/TypeNetwork/PageBot).
* Desktop application examples can be found in the separate a repository,
available under MIT Open Source license at [github.com/TypeNetwork/PageBotApp](https://github.com/TypeNetwork/PageBotApp).
* A growing library of real document examples are bundled in Examples, available under MIT Open Source license from [github.com/TypeNetwork/PageBotExamples](https://github.com/TypeNetwork/PageBotExamples)
* A manual, generated automatically with PageBot, is at [typenetwork.github.io/PageBot](https://typenetwork.github.io/PageBot)
* A website fully generated with PageBot can be found at [designdesign.space](http://designdesign.space). It also includes entry points for studies and workshops on how to work with PageBot.
* The TYPETR Upgrade website [upgrade.typenetwork.com](https://upgrade.typenetwork.com) is an example where the HTML/CSS code and all illustrations are generated by PageBot scripts.
"""
page = doc[1]
page.baselineGrid = LEADING
c = Composer(doc)
c.typeset(markDown=s, styles=styles)

tb = c.galleys[0].elements[0]
tb.fill = color('red')
print(tb.fill, tb.__class__.__name__)
tb.padding = p(2)
tb.parent = page
tb.w = COL
tb.conditions = (Left2Left(), Top2Top(), Fit2Height())

doc.solve()
doc.export('_export/TextBaselines.pdf')