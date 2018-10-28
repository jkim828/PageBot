# -----------------------------------------------------------------------------
#
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
#     20_PageBotPath_ABC.py
#
#     Draw a string outline as PageBotPath.
#     OSX-bug? --> Outlines of Roboto show with overlap.
#
from pagebot.toolbox.units import pt
from pagebot.contexts import getContext
from pagebot.elements.paths.pagebotpath import PageBotPath
from pagebot.fonttoolbox.objects.font import findFont

context = getContext()
context.newPage(1000, 500)
font = findFont('Roboto-Bold')
path = PageBotPath(context)
path.text('ABC', style=dict(font=font, fontSize=pt(400)))
path.translate((100, 100))

context.fill((1, 0, 0))
context.stroke(0, 10)
context.drawPath(path)