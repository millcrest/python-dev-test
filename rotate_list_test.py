import unittest
from rotate_list import rotate_list

class RotateListTests(unittest.TestCase):

    def test_rotation_by_zero(self):
        original_list = [1, 2, 3, 4, 5]
        rotated_list = rotate_list(original_list, 0)
        self.assertEqual(rotated_list, original_list)

    def test_rotation_by_positive_value(self):
        original_list = [1, 2, 3, 4, 5]
        rotated_list = rotate_list(original_list, 2)
        self.assertEqual(rotated_list, [4, 5, 1, 2, 3])

    def test_rotation_by_negative_value(self):
        original_list = [1, 2, 3, 4, 5]
        rotated_list = rotate_list(original_list, -3)
        self.assertEqual(rotated_list, [3, 4, 5, 1, 2])

    def test_rotation_with_empty_list(self):
        original_list = []
        rotated_list = rotate_list(original_list, 3)
        self.assertEqual(rotated_list, [])

if __name__ == '__main__':
    unittest.main()
