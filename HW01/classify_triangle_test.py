""" A test class for classifying triangles

    author: Fatih Izgi
    date: 04-Feb-2021
    python: v3.9.1
"""


import unittest
from classify_triangle import classify_triangle


class TestClassifyTriangle(unittest.TestCase):
    """ Test class of the methods """

    def test_triangle_invalid(self):
        """ test classify_triangle method for invalid inputs """

        # it is not possible to create a triangle with these values
        self.assertEqual(classify_triangle(3, 4, 9), 'invalid')
        self.assertEqual(classify_triangle(2, 6, 2), 'invalid')
        self.assertEqual(classify_triangle(8, 4, 4), 'invalid')

    def test_triangle_equilateral(self):
        """ test classify_triangle method for equilateral inputs """

        # all sides have the same length
        self.assertEqual(classify_triangle(1, 1, 1), 'equilateral')
        self.assertEqual(classify_triangle(2, 2, 2), 'equilateral')
        self.assertEqual(classify_triangle(3, 3, 3), 'equilateral')

    def test_triangle_isosceles(self):
        """ test classify_triangle method for isosceles inputs """

        # only one pair of sides have the same length
        self.assertEqual(classify_triangle(8, 8, 9), 'isosceles')
        self.assertEqual(classify_triangle(3, 4, 4), 'isosceles')
        self.assertEqual(classify_triangle(5, 4, 5), 'isosceles')

    def test_triangle_right(self):
        """ test classify_triangle method for right inputs """

        # a2 + b2 == c2
        self.assertEqual(classify_triangle(3, 4, 5), 'right')
        self.assertEqual(classify_triangle(5, 12, 13), 'right')
        self.assertEqual(classify_triangle(7, 24, 25), 'right')

    def test_triangle_scalene(self):
        """ test classify_triangle method for scalene inputs """

        # everything else
        self.assertEqual(classify_triangle(5, 6, 8), 'scalene')
        self.assertEqual(classify_triangle(10, 11, 12), 'scalene')
        self.assertEqual(classify_triangle(15, 18, 20), 'scalene')


if __name__ == '__main__':
    unittest.main(exit=False)
