# -*- coding: UTF-8 -*-
#
#    blurb.py
#
from __future__ import print_function
import re
import blurbwriter

class Blurb(object):
    """

    The ``Content`` is a wrapper around the filibuster ``BlurbWriter``
    of Erik van Blokland and Jonathan Hoefler. There is supposed to be only one instance of
    the writer installed in the system.
    """
    def __init__(self, content=None):
        if content is None:
            from pagebot.contributions.filibuster import content
        #from filibuster import content
        self.writer = blurbwriter.BlurbWriter(content.content())

    reNoTags = re.compile('\<[^\>]*|([^\<\>]*)')

    def getBlurb(self, type, cnt=None, noTags=True):
        u"""

        The ``getBlurb`` method answers a random generated blurb of ``type``.
        The full list of available types get be obtained by calling ``self.getContentType()``.

        """
        if cnt is not None:
            content = ' '.join(self.writer.write(type).split(' ')[:cnt])
        else:
            content = self.writer.write(type)
        if noTags:
            content = ''.join(self.reNoTags.findall(content))
        return content

    def getBlurbTypes(self):
        u"""

        The ``getBlurbTypes`` answers a list of names of all types of content blurbs
        that can can be generated by the writer.

        """
        return self.writer.keywords

blurb = Blurb() # Make the single instance of Blurb.

if __name__ == '__main__':
    w = blurb
    for t in w.getBlurbTypes():
        print(t, w.getBlurb(t))

    print(w.getBlurb('sports_headline'))
    print(w.getBlurb('filibuster_about'))
    print(w.getBlurb('aerospace_headline'))
    print(w.getBlurb('address'))
    print
    for i in range(10):
        print(w.getBlurb('politics_euro_headline'))
    #print(w.getBlurb('aerospace_headline', 3))
    #print(w.getBlurbTypes())

