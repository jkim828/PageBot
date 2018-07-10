#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens & Font Bureau
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supperting usage of Svg, https://pypi.python.org/pypi/svgwrite
# -----------------------------------------------------------------------------
#
#     svgcontext.py
#
#     https://svgwrite.readthedocs.io/en/master/
#
import os

from pagebot.toolbox.transformer import uniqueID
from pagebot.contexts.basecontext import BaseContext
from pagebot.contexts.builders.svgbuilder import svgBuilder
from pagebot.contexts.strings.htmlstring import HtmlString
from pagebot.style import DEFAULT_FONT_SIZE, DEFAULT_FONT_PATH
from pagebot.constants import *
from pagebot.toolbox.dating import seconds
from pagebot.toolbox.color import noColor

class SvgContext(BaseContext):
    """An SvgContext uses svgwrite to export as SVG drawing."""

    # In case of specific builder addressing, callers can check here.
    isSvg = True

    TMP_PATH = '/tmp/pagebot%s.' + FILETYPE_SVG

    # Used by the generic BaseContext.newString( )
    STRING_CLASS = HtmlString
    EXPORT_TYPES = (FILETYPE_SVG,)

    def __init__(self):
        """Constructor of SvgContext.

        >>> context = SvgContext()
        >>> context.saveDocument('~/SvgContext.%s' % FILETYPE_SVG)

        """
        self.b = svgBuilder
        self._filePath = self.TMP_PATH % uniqueID()
        self._fill = noColor
        self._stroke = noColor
        self._strokeWidth = pt(0)
        self._frameDuration = seconds(1)
        self._fontSize = DEFAULT_FONT_SIZE
        self._font = DEFAULT_FONT_PATH
        self._ox = pt(0) # Origin set by self.translate()
        self._oy = pt(0)
        self._rotate = 0
        
        self._gState = [] # Stack of graphic states.
        self.save() # Save current set of values on gState stack.

        self.newDrawing()

        self._path = None # Hold current open SVG path

    def newDocument(self, w, h):
        """Ignore for SvgContext, as Drawing open automatic if first page is created."""
        pass

    def saveDocument(self, path, multiPage=None):
        """Select other than standard DrawBot export builders here.
        Save the current image as path, rendering depending on the extension of the path file.
        In case the path starts with "_export", then create it directories.

        >>> context = SvgContext()
        >>> context.saveImage('_export/MyFile.svg')

        """
        self._drawing.save()
        self.checkExportPath(path)
        os.system('mv %s %s' % (self._filePath, path))

    saveImage = saveDocument # Compatible API with DrawBot

    def newPage(self, w, h):
        """Create a new SVG page.

        >>> context = SvgContext()
        >>> context.newPage(100, 100)
        """

    def newDrawing(self):
        """Clear output canvas, start new export file.

        >>> context = SvgContext()
        >>> context.newDrawing()
        """
        self._drawing = self.b.Drawing(self._filePath, profile='tiny')

    def rect(self, x, y, w, h):
        """Draw a rectangle in the canvas.

        >>> from pagebot.toolbox.color import Color
        >>> path = '~/SvgContext_rect.svg'
        >>> context = SvgContext()
        >>> context.fill((color(r=1, g=0, b=0.5)))
        >>> context.rect(pt(0), pt(100), pt(600), pt(200))
        >>> context.stroke(pt(0), pt(20))
        >>> context.fill((color(r=0.4, g=0.1, b=0.9)))
        >>> context.rect(pt(300), pt(150), pt(400), pt(600))
        >>> context.saveDocument(path)
        >>> #r = os.system('open %s' % path)
        """
        rect = self._drawing.rect(insert=((self._ox+x).pt, (self._oy+y).pt), size=(w.pt, h.pt), 
                           stroke_width=self._strokeWidth.pt,
                           stroke=self._stroke, fill=self._fill)
        self._drawing.add(rect)

    def oval(self, x, y, w, h):
        """Draw an oval in rectangle, where (x,y) is the bottom-left and size (w,h).

        >>> from pagebot.toolbox.color import color, blackColor
        >>> path = '~/SvgContext_oval.svg'
        >>> context = SvgContext()
        >>> context.fill(color(r=1, g=0, b=0.5))
        >>> context.oval(pt(0), pt(100), pt(600), pt(200))
        >>> context.stroke(blackColor, pt(20))
        >>> context.fill(color(r=0.4, g=0.1, b=0.9))
        >>> context.oval(pt(300), pt(150), pt(400), pt(600))
        >>> context.saveDocument(path)
        >>> #r = os.system('open %s' % path)
        """
        oval = self._drawing.ellipse(center=((self._ox+x+w/2).pt, (self._oy+y+h/2).pt), r=((w/2).pt, (h/2).pt), 
                                             stroke_width=self._strokeWidth,
                                             stroke=self._stroke, fill=self._fill)
        self._drawing.add(oval)

    def circle(self, x, y, r):
        """Circle draws a DrawBot oval with (x,y) as middle point and radius r.

        >>> from pagebot.toolbox.color import color, blackColor
        >>> path = '~/SvgContext_circle.svg'
        >>> context = SvgContext()
        >>> context.fill(color(r=1, g=0, b=0.5))
        >>> context.circle(pt(0), pt(100), pt(300))
        >>> context.stroke(blackColor, pt(20))
        >>> context.fill(color(r=0.6, g=0.1, b=0.5))
        >>> context.circle(pt(300), pt(150), pt(200))
        >>> context.saveDocument(path)
        >>> #r = os.system('open %s' % path)
        """
        circle = self._drawing.circle(center=((self._ox+x+r).pt, (self._oy+y+r).pt), r=r.pt, 
                                      stroke_width=self._strokeWidth, 
                                      stroke=self._stroke, fill=self._fill)
        self._drawing.add(circle)

    def line(self, p1, p2):
        """Draw a line from p1 to p2.

        >>> path = '~/SvgContext_line.svg'
        >>> context = SvgContext()
        >>> context.stroke((1, 0, 0.5), 30)
        >>> context.line((0, 100), (300, 300))
        >>> context.stroke((0.6, 0.1, 0.5), 20)
        >>> context.line((300, 150), (200, 100))
        >>> context.saveDocument(path)
        >>> #r = os.system('open %s' % path)
        """
        line = self._drawing.line(((self._ox+p1[0]).r, (self._oy+p1[1]).pt), ((self._ox+p2[0]).pt, (self._oy+p2[1]).pt), 
                                  stroke_width=self._strokeWidth, 
                                  stroke=self._stroke)
        self._drawing.add(line)

    def setFillColor(self, c):
        if c is noColor:
            self._fill = 'none'
        else:
            r, g, b = c.rgb
            self._fill = self.b.rgb(100*r, 100*g, 100*b, '%')

    fill = setFillColor

    def setStrokeColor(self, c, strokeWidth=None):
        if c is noColor:
            self._fill = 'none'
        else:
            r, g, b = c.rgb
            self._fill = self.b.rgb(100*r, 100*g, 100*b, '%')
        self._strokeWidth = (strokeWidth or pt(1)).v

    stroke = setStrokeColor

    def saveGraphicState(self):
        """Save the current graphic state.

        >>> context = SvgContext()
        >>> context.font('Verdana')
        >>> context._font
        'Verdana'
        >>> context.save()
        >>> context.font('Verdana-Bold')
        >>> context._font
        'Verdana-Bold'
        >>> context.restore()
        >>> context._font
        'Verdana'
        """
        gState = dict(
            font=self._font,
            fontSize=self._fontSize,
            fill=self._fill,
            stroke=self._stroke,
            strokeWidth=self._strokeWidth,
            ox=self._ox,
            oy=self._oy,
            rotate=self._rotate,
        )
        self._gState.append(gState)

    save = saveGraphicState

    def restoreGraphicState(self):
        gState = self._gState.pop()
        self._font = gState['font']
        self._fontSize = gState['fontSize']
        self._fill = gState['fill']
        self._stroke = gState['stroke']
        self._strokeWidth = gState['strokeWidth']
        self._ox = gState['ox']
        self._oy = gState['oy']
        self._rotate = gState['rotate']

    restore = restoreGraphicState
    
    #   T E X T 

    def fontSize(self, fontSize):
        """Set the current graphic state to fontSize.

        """
        self._fontSize = fontSize

    def font(self, font, fontSize=None):
        """Set the current graphic state to font. 
        TODO: Make this match the font.path.
        """
        self._font = font
        if fontSize is not None:
            self.fontSize(fontSize)

    def text(self, sOrBs, p):
        """Draw the sOrBs text string, can be a str or BabelString, including a DrawBot FormattedString
        at position p.

        >>> path = '~/SvgContext_text.svg'
        >>> context = SvgContext()
        >>> context.fontSize(pt(100))
        >>> context.font('Verdana-Bold') # TODO: Match with font path.
        >>> context.fill(color(r=1, g=0, b=0.5))
        >>> context.text('ABCDEF', (pt(100), pt(200)))
        >>> context.fill(color(r=1, g=0, b=1))
        >>> context.stroke(color(r=0.5, g=0, b=0.5), pt(5))
        >>> context.text('ABCDEF', (pt(100), pt(300)))
        >>> context.saveDocument(path)
        >>> #r = os.system('open %s' % path)

        """
        if not isinstance(sOrBs, str):
            sOrBs = sOrBs.s # Assume here is's a BabelString with a FormattedString inside.
        t = self._drawing.text(sOrBs, insert=(p[0].pt, p[1].pt), 
                               stroke=self._stroke, stroke_width=self._strokeWidth,
                               fill=self._fill, font_size=self._fontSize, font_family=self._font)
        self._drawing.add(t)

    def textBox(self, sOrBs, r):
        """Draw the sOrBs text string, can be a str or BabelString, including a DrawBot FormattedString
        in rectangle r."""
        if not isinstance(sOrBs, str):
            sOrBs = sOrBs.s # Assume here is's a BabelString with a FormattedString inside.
        x, y, w, h = r
        t = self._drawing.text(sOrBs, insert=(x.pt, y.pt),
                               stroke=self._stroke, stroke_width=self._strokeWidth,
                               fill=self._fill, font_size=self._fontSize.pt, font_family=self._font)
        self._drawing.add(t)

    def translate(self, dx, dy):
        """Translate the origin by (dx, dy)."""
        self._ox += dx
        self._oy += dy

    def rotate(self, angle):
        """Rotate by angle."""
        self._rotate = angle

    def textSize(self, s):
        return pt(100, 20)

    #   A N I M A T I O N

    def frameDuration(self, secondsPerFrame):
        """Set the frame duretion for animated gifs to a number of seconds per frame."""
        self._frameDuration = secondsPerFrame

if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])
