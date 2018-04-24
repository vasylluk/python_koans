#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    pass

    s1,s2,s3 =a,b,c
    sides = [s1,s2,s3]

    l = lambda i: i<0
    neg = [l(i) for i in sides]
    if 0 in sides:
    	raise(TriangleError)
    elif True in neg:
    	raise(TriangleError)
    if sides.count(1)==2 or sides.count(2)==2:
    	raise(TriangleError)

    if sides.count(s1)==3:
    	return 'equilateral'
    if sides.count(s1)==2 or sides.count(s3)==2:
    	return 'isosceles'
    return 'scalene'
# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
