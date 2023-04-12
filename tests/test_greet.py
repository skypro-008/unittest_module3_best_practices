import unittest
from unittest.mock import Mock

from parameterized import parameterized

import src.greet as greet


class TestGreet(unittest.TestCase):
    def setUp(self):
        self.mock_greeting = Mock(return_value='Good evening')

    def test_greet(self):
        self.assertEqual(greet.greet('Jane', self.mock_greeting), 'Good evening, Jane.')

    def test_greet_list(self):
        self.assertEqual(greet.greet_list(['John', 'Jane'], self.mock_greeting),
                         ['Good evening, John.', 'Good evening, Jane.'])

    @parameterized.expand([
        ('morning', 6, 'Good morning'),
        ('afternoon', 15, 'Good afternoon'),
        ('evening', 21, 'Good evening'),
    ])
    def test_read_greeting(self, name, hour, expected):
        # Mock метода datetime.now(), чтобы возвращалось фиксированное время
        datetime_mock = Mock()
        datetime_mock.now.return_value.hour = hour
        with unittest.mock.patch('src.greet.datetime', datetime_mock):
            self.assertEqual(greet.read_greeting(), expected)


if __name__ == '__main__':
    unittest.main()
