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
#     brochure.py
#
from pagebot.conditions import *
from pagebot.publications.publication import Publication
from pagebot.elements import *


class Brochure(Publication):
    """Create a default brochure, with cover/home page, article pages in different 
    template layouts, table of content, navigation. Layout and content options defined 
    by external parameters.
    The brochure should be optimized to export as PDF as well as website.

    Subclassed from Document-->Publication with the following optional attributes:
    rootStyle=None, styles=None, views=None, name=None, cssClass=None, title=None,
    autoPages=1, defaultTemplate=None, templates=None, originTop=True, startPage=0,
    w=None, h=None, exportPaths=None, **kwargs)

    >>> from pagebot.constants import A4
    >>> br = Brochure()
    >>> br.export('_export/Brochure.pdf')
    """

    DEFAULT_COVERBACKGROUND = (0.3, 0.6, 0.3)

    def initialize(self, coverBackgroundFill=None, **kwargs):
        u"""Initialize the generic brochure templates. """

        padding = self.css('pt'), self.css('pr'), self.css('pb'), self.css('pl')
        w, h = self.w, self.h
        gridY = [(None, 0)] # Default is full height of columns, not horizontal division.

        if coverBackgroundFill is None:
            coverBackgroundFill = self.DEFAULT_COVERBACKGROUND

        t = Template(w=w, h=h, name='Cover', padding=padding, gridY=gridY)
        newRect(parent=t, conditions=[Fit2Sides()], name='Cover', fill=coverBackgroundFill)
        newTextBox(parent=t, conditions=[Fit2Width(), Top2Top()], name='Title', h=200)
        self.addTemplate(t.name, t)
        score = t.solve()

        t = Template(w=w, h=h, name='Title Page', padding=padding, gridY=gridY)
        newPlacer(parent=t, conditions=[Left2Col(1), Bottom2Row(0)], name='Title', h=200)
        self.addTemplate(t.name, t)
        t.solve(score)

        t = Template(w=w, h=h, name='Table Of Content', padding=padding, gridY=gridY)
        newPlacer(parent=t, conditions=[Right2Right(), Top2Top(), Fit2Height()], name='TOC', w=200)
        self.addTemplate(t.name, t)
        t.solve(score)

        t = Template(w=w, h=h, name='Main Page', padding=padding, gridY=gridY)
        newPlacer(parent=t, conditions=[Right2Right(), Top2Top(), Fit2Height()], name='Main Column', w=200)
        self.addTemplate('default', t)
        t.solve(score)

        t = Template(w=w, h=h, name='Register Page', padding=padding, gridY=gridY)
        newPlacer(parent=t, conditions=[Right2Right(), Top2Top(), Fit2Height()], name='Register', w=200)
        self.addTemplate(t.name, t)
        t.solve(score)

        if score.fails:
            print('Score', score)
            for failed in score.fails:
                print('\t', failed)
