"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """
    Test the calculator module
    """

    def test_add(self):
        """
        Test the addition
        :return:
        """
        res = calc.add(2, 3)
        self.assertEqual(res, 5)

    def test_subtract(self):
        """
        Test the subtraction
        :return:
        """
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
