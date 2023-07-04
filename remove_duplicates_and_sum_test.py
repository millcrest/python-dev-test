import unittest
from remove_duplicates_and_sum import remove_duplicates_and_sum

class RemoveDuplicatesAndSumTests(unittest.TestCase):

    def test_removing_duplicates_and_summation(self):
        original_list = [1, 2, 2, 3, 4, 4, 5, 5]
        unique_list, total_sum = remove_duplicates_and_sum(original_list)
        self.assertEqual(unique_list, [1, 3])
        self.assertEqual(total_sum, 4)

    def test_removing_duplicates_and_summation_with_empty_list(self):
        original_list = []
        unique_list, total_sum = remove_duplicates_and_sum(original_list)
        self.assertEqual(unique_list, [])
        self.assertEqual(total_sum, 0)

    def test_removing_duplicates_and_summation_with_single_element(self):
        original_list = [10]
        unique_list, total_sum = remove_duplicates_and_sum(original_list)
        self.assertEqual(unique_list, [10])
        self.assertEqual(total_sum, 10)

if __name__ == '__main__':
    unittest.main()
