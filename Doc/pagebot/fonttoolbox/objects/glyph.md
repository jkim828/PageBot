# fonttoolbox.objects.glyph


## Functions

### NSFont
### C
float(x) -> floating point number

Convert a string or number to a floating point number, if possible.
### TTFont
The main font object. It manages file input and output, and offers
	a convenient way of accessing tables.
	Tables will be only decompiled when necessary, ie. when they're actually
	accessed. This means that simple operations can be extremely fast.
### TTLibError
### GlyphAnalyzer
### Point
Point object containing Cartesian coordinates plus on / offcurve boolean.

    >>> p = Point(101, 303, True)
    >>> p.onCurve is False
    False

    >>> print p
    Pt(101,303,On)
### F
float(x) -> floating point number

Convert a string or number to a floating point number, if possible.
### FontInfo
Read-only access to font information, such as names, character set and supported
OpenType features.
### Glyph
The Glyph class wraps the glyph structure of a TrueType Font and
extracts data from the raw glyph such as point sequence and type.

    >>> import pagebot
    >>> from pagebot.toolbox.transformer import getFontPath
    >>> p = getFontPath('AmstelvarAlpha-VF')
    >>> from pagebot.fonttoolbox.objects.font import Font
    >>> f = Font(p, install=False)
    >>> g = f['a']
    >>> g.name
    'a'

    >>> len(g.points)
    40

    >>> g.points[-1].onCurve
    False

    >>> contours = g.contours
    >>> len(contours)
    2

    >>> path = g.path
    >>> print path
    <BezierPath>

    >>> nspath = path.getNSBezierPath()
    >>> bounds = nspath.bounds()
    >>> print bounds
    <NSRect origin=<NSPoint x=38.0 y=-15.0> size=<NSSize width=948.0 height=1037.0>>

    >>> len(bounds)
    2

    >>> len(bounds[0])
    2

    >>> len(bounds[1])
    2

    >>> print bounds[0]
    <NSPoint x=38.0 y=-15.0>

    >>> bounds[0][0]
    38.0
### Segment
Curve segment from a certain oncurve point to the next one.

    >>> p0 = Point(101, 303, True)
    >>> p1 = Point(202, 404, False)
    >>> p2 = Point(303, 808, False)
    >>> p3 = Point(909, 808, True)
    >>> points = [p0, p1, p2, p3]
    >>> s = Segment(points)
    >>> len(s)
    4

    >>> p4 = Point(111, 313, False)
    >>> s.append(p4)
    >>> len(s)
    5

    >>> s.points[-1].onCurve
    False
### function point2D
Answer the 2D origin as combination of p and offset.