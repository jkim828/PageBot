# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens & Font Bureau
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#     Made for usage in DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     PBFormattedString.py
#
#     Can be used to experiment with the DrawBot FormattedString class.
#
fs = FormattedString('')

class PBFormattedString(fs.__class__):
    pass
    
f = PBFormattedString('AAA', font='Verdana', fontSize=300, fill=(1, 0, 0))
text(f, (100 ,100))

