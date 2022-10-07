#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 7/3/2021 12:27 AM
# @Author : Michael Reda
# @File : polevector_position.py
# ---------------------------------
# import libraries
import maya.cmds as cmds
import maya.api.OpenMaya as om
# ---------------------------------


def get_postion(node):
    return cmds.xform(node, q=1, ws=1, t=1)

def get_vector(postion):
    return om.MVector(postion[0], postion[1], postion[2])

def make_locator(pos):
    loc = cmds.spaceLocator(n="poleVector_loc#")[0]
    grp = cmds.group(loc, n=loc+"_offset_grp#")
    cmds.xform(grp, t=pos)
    return grp

def make_polevector_ctrl(jnt_list, offset=3):
    """

    :param jnt_list:
    :param offset:
    :return:
    """
    if len(jnt_list) != 3:
        raise Exception("You must make polevector control to 3 joints")

    # getting positions
    start_pos = get_postion(jnt_list[0])
    mid_pos = get_postion(jnt_list[1])
    end_pos = get_postion(jnt_list[2])

    # getting vectors
    start_vector = get_vector(start_pos)
    mid_vector = get_vector(mid_pos)
    end_vector = get_vector(end_pos)

    # the mid point between start and end
    ratio = (mid_vector-start_vector).length()/(end_vector-start_vector).length()

    mid_point_vector = ((end_vector-start_vector)*ratio)+start_vector

    pole_vector_pos = ((mid_vector-mid_point_vector)*offset)+mid_vector
    poleVector_loc = make_locator(pole_vector_pos)

    cmds.delete(cmds.aimConstraint(jnt_list[1], poleVector_loc, mo=0))


# Main function
def main():
    make_polevector_ctrl(cmds.ls(sl=1), offset=3)


if __name__ == '__main__':
    print(("-" * 20) + "\nStart of code...\n" + ("-" * 20))
    main()
    print(("-" * 20) + "\nEnd of code.\n" + ("-" * 20))
