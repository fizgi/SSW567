""" A script for classifying triangles

    author: Fatih Izgi
    date: 04-Feb-2021
    python: v3.9.1
"""


def classify_triangle(a: float, b: float, c: float):
    sides = sorted([a, b, c])

    if sides[0] + sides[1] <= sides[2]:  # it is not possible to create a triangle with these values
        return 'invalid'
    elif len(set(sides)) == 1:  # all sides have the same length
        return 'equilateral'
    elif len(set(sides)) == 2:  # only one pair of sides have the same length
        return 'isosceles'
    elif sides[0]**2 + sides[1]**2 == sides[2]**2:  # a2 + b2 == c2
        return 'right'
    else:
        return 'scalene'
