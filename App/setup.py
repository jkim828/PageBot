# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#    Copyright (c) 2016+ Type Network
#
#
# -----------------------------------------------------------------------------
#
#    python setup.py py2app
#

"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

setup(
    app=['appdelegate.py'],
    name="PageBot",
    data_files=['en.lproj'],#, '../fonts'],
    setup_requires=['py2app'],
    options=dict(py2app=dict(iconfile='en.lproj/pagebot.icns', packages=['drawBot', 'pagebot', 'lxml']))#, 'markdown', 'robofab', 'mutatorMath', 'fontMath']))
)
