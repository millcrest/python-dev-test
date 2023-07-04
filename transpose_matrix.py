import unittest


def transpose_matrix(matrix):
    if not matrix:
        return []  # Return empty list for empty matrix

    transposed = []

    # Your code goes here

    return transposed


class TransposeMatrixTests(unittest.TestCase):
    def test_transpose_square_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertEqual(transpose_matrix(matrix), expected_output)

    def test_transpose_rectangular_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        expected_output = [[1, 4], [2, 5], [3, 6]]
        self.assertEqual(transpose_matrix(matrix), expected_output)

    def test_transpose_empty_matrix(self):
        matrix = []
        expected_output = []
        self.assertEqual(transpose_matrix(matrix), expected_output)

    def test_transpose_single_row_matrix(self):
        matrix = [[1, 2, 3, 4]]
        expected_output = [[1], [2], [3], [4]]
        self.assertEqual(transpose_matrix(matrix), expected_output)


if __name__ == "__main__":
    unittest.main()
