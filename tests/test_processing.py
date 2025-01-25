import unittest
from bank_project.processing.sort_by_date import sort_by_date



class TestProcessing(unittest.TestCase):
    def test_sort_by_date_ascending(self):
        unsorted_data = [
            {"date": "2023-01-05"},
            {"date": "2023-02-03"},
            {"date": "2023-01-15"}
        ]
        expected_output = [
            {"date": "2023-01-05"},
            {"date": "2023-01-15"},
            {"date": "2023-02-03"}
        ]
        actual_output = sort_by_date(unsorted_data)
        self.assertEqual(actual_output, expected_output)

    def test_sort_by_date_descending(self):
        unsorted_data = [
            {"date": "2023-04-20"},
            {"date": "2023-06-30"},
            {"date": "2023-08-25"}
        ]
        expected_output = [
            {"date": "2023-08-25"},
            {"date": "2023-06-30"},
            {"date": "2023-04-20"}
        ]
        actual_output = sort_by_date(unsorted_data, reverse=True)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()