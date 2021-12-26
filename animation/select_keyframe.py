#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Documentation: 
"""

# @Time : 27-Dec-21 12:36 AM
# @File : select_keyframe.py

__version__ = "1.0.1"
__author__ = "Michael Reda"
__email__ = "eng.michaelreda@gmail.com"
__license__ = "GPL"
__copyright__ = "Copyright 2021, Michael Reda"
__status__ = "Beta"

# ---------------------------------
# import libraries
import maya.cmds as cmds

# ---------------------------------
def select_current_keyframes():
    """
    To select the current keyframes of selected channels
    :return: None
    """
    cmds.selectKey(cl=1)
    attrs = cmds.selectionConnection("graphEditor1FromOutliner", q=1, object=1)
    current_frame = cmds.currentTime(q=1)
    for attr in attrs:
        if cmds.keyframe(attr, q=1, kc=1) == 0:
            continue
        cmds.selectKey(attr, add=1, t=(current_frame,))


# Main function
def main():
    select_current_keyframes()


if __name__ == '__main__':
    main()

