import unittest
from testing_functions import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py' """

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('David', 'Richard')
        self.assertEqual(formatted_name, 'David Richard')

    def test_first_middle_last_name(self):
        """Do like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()

