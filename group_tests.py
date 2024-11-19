import unittest
from group import groups_of_3

class TestCases(unittest.TestCase):
    #task 1
    def test_groups(self):
        self.assertEqual(groups_of_3([1, 2, 3, 4, 5, 6, 7, 8, 9]), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_less_than_three_elements(self):
        self.assertEqual(groups_of_3([1, 2]), [[1, 2]])

    #task 2
