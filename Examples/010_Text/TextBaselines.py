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
from pagebot.constants import GRID_LINE, GRID_COL, GRID_SQR, GRID_ROW, LANGUAGE_EN
from pagebot.toolbox.units import p, pt, em
from pagebot.toolbox.color import color
from pagebot.typesetter import Typesetter
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.conditions import *

COL = p(26) # Column width
GUTTER = p(2) # Gutter width
COLS = 3 # Number of columns
PADDING = p(5) # Padding of the page
PS = pt(16) # Fontsize of body text
LEADING = 1.4*PS

# Calculate the width of the page from the column measures
W = COLS * COL + (COLS-1) * GUTTER + 2*PADDING
H = 1000 # Fixed height

GRIDX = [] # Construct the column grid measures
for n in range(COLS-1):
    GRIDX.append((COL, GUTTER))
GRIDX.append((COL, p(0))) # Last column does not have gutter

font = findFont('Verdana')

h1Style = dict(font=font, fontSize=1.5*PS, textFill=(1, 0, 0), leading=LEADING)
h2Style = dict(font=font, fontSize=1.2*PS, textFill=(1, 0, 0.5), leading=LEADING,
    paragraphTopSpacing=LEADING)
pStyle = dict(font=font, fontSize=PS, leading=LEADING)
liStyle = dict(font=font, fontSize=PS, indent=pt(8), firstLineIndent=0, leading=LEADING)
styles = dict(font=font, h1=h1Style, h2=h2Style, p=pStyle, li=liStyle, ul=liStyle, bullet=liStyle)

# Create a document with these attributes, single page.
doc = Document(w=W, h=H, padding=PADDING, gridX=GRIDX, originTop=False, styles=styles,
    baselineGrid=LEADING, language=LANGUAGE_EN)
view = doc.view
view.showTextBoxBaselines = True
view.showTextBoxY = True
view.showBaselineGrid = [GRID_LINE] # Set the view to show the baseline grid
view.showGrid = [GRID_COL, GRID_ROW, GRID_SQR] # Set the view to display the grid

s = """

# What is PageBot?

PageBot is a page layout program that enables designers to create high quality documents using code. It is available both as Python library working with [DrawBot](http://www.drawbot.com) and as part of a collection of stand-alone desktop applications that can be created from it. Other contexts such as [Flat](http://xxyxyz.org/flat) (currently under development) allow PageBot to run environments other Mac OS X, for example on web servers. Initiated by [Type Network](https://typenetwork.com), the aim is to create a system for scriptable applications generating professionally designed documents that use high quality typography.

## Some PageBot attributes

* The core library, tutorial and basic examples for PageBot are available under MIT Open Source license from [github.com/TypeNetwork/PageBot](https://github.com/TypeNetwork/PageBot).
* Desktop application examples can be found in the separate a repository, available under MIT Open Source license at [github.com/TypeNetwork/PageBotApp](https://github.com/TypeNetwork/PageBotApp).
* A growing library of real document examples are bundled in Examples, available under MIT Open Source license from [github.com/TypeNetwork/PageBotExamples](https://github.com/TypeNetwork/PageBotExamples)
* A website fully generated with PageBot can be found at [designdesign.space](http://designdesign.space). It also includes entry points for studies and workshops on how to work with PageBot.
* The TYPETR Upgrade website [upgrade.typenetwork.com](https://upgrade.typenetwork.com) is an example where the HTML/CSS code and all illustrations are generated by PageBot scripts.
"""
page = doc[1]
page.baselineGrid = LEADING
t = Typesetter(doc.context, styles=styles)
galley = t.typesetMarkdown(s)

tb1 = galley.elements[0]
tb1.fill = 0.95
tb1.padding = p(0.5)
tb1.parent = page
tb1.w = COL
#tb.conditions = (Left2Left(), Top2Top(), Fit2Height(), Baseline2Grid(index=0))
tb1.conditions = (Left2Left(), Top2Top(), Fit2Height())

for textLine in tb1.textLines:
    print(textLine.y, textLine)

tb2 = tb1.copy(parent=page)
tb2.fill = 0.9
tb2.conditions = (Left2Col(1), Top2Top(), Fit2Height())

tb3 = tb2.copy(parent=page)
tb3.fill = 0.85
tb3.conditions = (Left2Col(2), Top2Top(), Fit2Height())

doc.solve()
doc.export('_export/TextBaselines.pdf')