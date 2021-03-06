# -*- coding: UTF-8 -*-
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
#     AutomaticPageComposition.py
#
#     This script generates an article in Dustch the apporach to
#     generate automatic layouts, using Galley, Typesetter and Composer classes.
#
#     BROKEN: Needs to update Element interfaces.
#
from pagebot.style import getRootStyle
from pagebot.constants import LEFT
from pagebot.document import Document
from pagebot.elements import *
from pagebot.composer import Composer
from pagebot.typesetter import Typesetter
from pagebot.toolbox.units import em

SHOW_TIMER = False

SHOW_FLOW_CONNECTIONS = True

if SHOW_GRID:
    BOX_COLOR = (0.8, 0.8, 0.8, 0.4)
else:
    BOX_COLOR = None

# Get the default root style and overwrite values for this document.
U = 7
baselineGrid = 2*U
listIndent = 2*U

RS = getRootStyle(
    u = U, # Page base unit
    # Basic layout measures altering the default rooT STYLE.
    w = 595, # Om root level the "w" is the page width 210mm, international generic fit.
    h = 11 * 72, # Page height 11", international generic fit.
    ml = 7*U, # Margin left rs.mt = 7*U # Margin top
    baselineGrid = 14,#baselineGrid,
    gw = 2*U, # Generic gutter, equal for width and height
    gd = 2*U,
    # Column width. Uneven means possible split in 5+1+5 or even 2+1+2 +1+ 2+1+2
    # 11 is a the best in that respect for column calculation.
    cw = 11*U,
    ch = 6*baselineGrid - U, # Approx. square and fitting with baseline.
    listIndent = listIndent, # Indent for bullet lists
    listTabs = [(listIndent, LEFT)], # Match bullet+tab with left indent.
    # Display option during design and testing
    BOX_COLOR = BOX_COLOR,
    # Text measures
    leading = 14,
    fontSize = 9
)
RS['language'] = 'nl-be' # Make Dutch hyphenation.
MD_PATH = 'testPaginaCompositie_nl.md'
EXPORT_PATH = 'export/TestPaginaOpmaak.pdf'

MAIN_FLOW = 'main' # ELement id of the text box on pages the hold the main text flow.

# Tracking presets
H1_TRACK = H2_TRACK = em(0.015) # 1/1000 of fontSize, multiplier factor.
H3_TRACK = em(0.030) # Tracking as relative factor to font size.
P_TRACK = em(0.030)

VARS = True

BOOK = MEDIUM = 'Verdana'
BOOK_ITALIC = 'Verdana-Italic'
BOLD = SEMIBOLD = 'Verdana-Bold'
# -----------------------------------------------------------------
def makeDocument(rs):
    """Demo page composer."""

    # Set some values of the default template (as already generated by the document).
    # Make squential unique names for the flow boxes inside the templates
    flowId0 = MAIN_FLOW+'0'
    flowId1 = MAIN_FLOW+'1'
    flowId2 = MAIN_FLOW+'2'

    # Template 1
    template1 = Template(rs) # Create template of main size. Front page only.
    # Show grid columns and margins if rootStyle.showGrid or rootStyle.showGridColumns are True
    template1.grid(rs)
    # Show baseline grid if rs.showBaselines is True
    template1.baselineGrid(rs)
    # Create empty image place holders. To be filled by running content on the page.
    template1.cContainer(4, 0, 2, 4, rs)  # Empty image element, cx, cy, cw, ch
    template1.cContainer(0, 5, 2, 3, rs)
    # Create linked text boxes. Note the "nextPageName" to keep on the same page or to next.
    template1.cTextBox('', 0, 0, 2, 5, rs, flowId0, nextBoxName=flowId1, nextPageName=0, fill=BOX_COLOR)
    template1.cTextBox('', 2, 0, 2, 8, rs, flowId1, nextBoxName=flowId2, nextPageName=0, fill=BOX_COLOR)
    template1.cTextBox('', 4, 4, 2, 4, rs, flowId2, nextBoxName=flowId0, nextPageName=1, fill=BOX_COLOR)
    # Create page number box. Pattern pageNumberMarker is replaced by actual page number.
    template1.cText(rs['pageNumberMarker'], 6, 0, rs, font=BOOK, fontSize=12, fill=BOX_COLOR)

    # Template 2
    template2 = Template(rs) # Create second template. This is for the main pages.
    # Show grid columns and margins if rootStyle.showGrid or rootStyle.showGridColumns are True
    template2.grid(rs)
    # Show baseline grid if rs.showBaselines is True
    template2.baselineGrid(rs)
    template2.cContainer(4, 0, 2, 3, rs)  # Empty image element, cx, cy, cw, ch
    template2.cContainer(0, 5, 2, 3, rs)
    template2.cContainer(2, 2, 2, 2, rs)
    template2.cContainer(2, 0, 2, 2, rs)
    template2.cContainer(4, 6, 2, 2, rs)
    template2.cTextBox('', 0, 0, 2, 5, rs, flowId0, nextBoxName=flowId1, nextPageName=0, fill=BOX_COLOR)
    template2.cTextBox('', 2, 4, 2, 4, rs, flowId1, nextBoxName=flowId2, nextPageName=0, fill=BOX_COLOR)
    template2.cTextBox('', 4, 3, 2, 3, rs, flowId2, nextBoxName=flowId0, nextPageName=1, fill=BOX_COLOR)
    # Create page number box. Pattern pageNumberMarker is replaced by actual page number.
    template2.cText(rs['pageNumberMarker'], 6, 0, rs, font=BOOK, fontSize=12, fill=BOX_COLOR)

    # Create new document with (w,h) and fixed amount of pages.
    # Make number of pages with default document size.
    # Initially make all pages default with template2
    doc = Document(rs, autoPages=2, template=template2)

    # Cache some values from the root style that we need multiple time to create the tag styles.
    sFontSize = rs['fontSize']
    sLeading = rs['leading']
    sListIndent = rs['listIndent']
    sLanguage = rs['language']

    # Add styles for whole document and text flows.
    # Note that some values are defined here for clarity, even if their default root values
    # are the same.
    doc.newStyle(name='chapter', font=BOOK)
    doc.newStyle(name='title', fontSize=3*sFontSize, font=BOLD)
    doc.newStyle(name='subtitle', fontSize=2*sFontSize, font=BOOK_ITALIC)
    doc.newStyle(name='author', fontSize=2*sFontSize, font=BOOK, fill=color(1, 0, 0))
    doc.newStyle(name='h1', fontSize=3*sFontSize, font=SEMIBOLD, fill=color(1, 0, 0),
        leading=2*sFontSize, tracking=H1_TRACK, postfix='\n')
    doc.newStyle(name='h2', fontSize=2*sFontSize, font=SEMIBOLD, fill=color(0, 0.5, 1),
        leading=1*sFontSize, tracking=H2_TRACK, postfix='\n')
    doc.newStyle(name='h3', fontSize=2*sFontSize, font=MEDIUM, fill=blackColor,
        leading=1*sFontSize, rNeedsBelow=2*leading, tracking=H3_TRACK,
        postfix='\n')

    # Spaced paragraphs.
    doc.newStyle(name='p', fontSize=sFontSize, font=BOOK, fill=color(0.1), prefix='', postfix='\n',
        tracking=P_TRACK, sLeading=14, xTextAlign=LEFT, hyphenation=True)
    doc.newStyle(name='b', font=SEMIBOLD)
    doc.newStyle(name='em', font=BOOK_ITALIC)
    doc.newStyle(name='hr', stroke=color(1, 0, 0), strokeWidth=4)
    doc.newStyle(name='br', postfix='\n') # Simplest way to make <br/> be newline
    doc.newStyle(name='img', leading=sLeading, fontSize=sFontSize, font=BOOK,)

    # Footnote reference index.
    doc.newStyle(name='sup', font=MEDIUM, baselineShift=em(0.6),
        fontSize=0.65*sFontSize)
    doc.newStyle(name='li', fontSize=sFontSize, font=BOOK,
        tracking=P_TRACK, leading=sLeading, hyphenation=True,
        # Lists need to copy the listIndex over to the regalar style value.
        tabs=[(listIndent, LEFT)], indent=sListIndent,
        firstLineIndent=1, postfix='\n')
    doc.newStyle(name='ul',)
    doc.newStyle(name='literatureref', fill=0.5, baselineShift=em(0.2), fontSize=0.8*sFontSize)
    doc.newStyle(name='footnote', fill=color(1, 0, 0), fontSize=0.8*U, font=BOOK)
    doc.newStyle(name='caption', tracking=P_TRACK, language=sLanguage, fill=color(0.2),
        leading=0.8*sLeading, fontSize=0.8*sFontSize, font=BOOK_ITALIC,
        indent=U/2, tailIndent=-U/2, hyphenation=True)

    # Change template of page 1
    page1 = doc[1]
    page1.setTemplate(template1)

    AA = """Waar in de traditionele manier van werken met opmaakprogrammatuur."""
    aa = """Waar in de traditionele manier van werken met opmaakprogrammatuur zoals Quark XPress en InDesign altijd een menselijke beslissing de definitieve opmaak van een pagina bepaalt, zijn er steeds meer situaties waarin dat geen optie is. Doordat steeds meer pagina’s worden gegenereerd met inhoud die uit een database komt – of van een online source – en waar de selectie van de informatie direct wordt bepaald door eigenschappen van de lezer, moet de layout van de pagina’s automatisch worden berekend. Er bestaat op het moment vreemd genoeg geen digitaal gereedschap dat enerzijds voldoende flexibel is om in alle mogelijk technieken en soorten layouts te gebruiken, te koppelen is met een grote verscheidenheid aan informatiebronnen, en anderzijds voldoet aan de typografische eisen die aan handmatige opmaak worden gesteld. """*5

    tb = page0.getElement(flowId0)
    print(tb)
    hyphenation(True)
    language('nl-be')
    tb.append(FormattedString(AA+'\n', fontSize=20, lineHeight=28))
    aa = tb.append(FormattedString(aa, fontSize=10, lineHeight=14))
    tb = page0.getElement(flowId1)
    aa = tb.append(aa)
    tb = page0.getElement(flowId2)
    aa = tb.append(aa)

    """
    # Create main Galley for this page, for pasting the sequence of elements.
    g = Galley()
    t = Typesetter(doc, g)
    t.typesetFile(MD_PATH)

    # Fill the main flow of text boxes with the ML-->XHTML formatted text.
    c = Composer(doc)
    c.compose(g, doc[1], flowId0)
    """
    return doc

d = makeDocument(RS)
d.export(EXPORT_PATH)

