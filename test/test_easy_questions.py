import unittest

from src.easy_questions import fibonacci
from src.easy_questions import is_palindrome
from src.easy_questions import odd_even_bit_swap


class EasyQuestionsTests(unittest.TestCase):

    def test_fibonacci(self):
        small_fibonacci_test_sequence = [
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377
        ]

        for i in range(len(small_fibonacci_test_sequence)):
            actual = fibonacci(i)
            self.assertEqual(small_fibonacci_test_sequence[i], actual)

        expected = 280571172992510140037611932413038677189525
        actual = fibonacci(200)
        self.assertEqual(expected, actual)

    def test_is_palindrome(self):
        palindromes = [
            'mom',
            'race car',
            '!r a^c e  ca *(r*&',
            '""',
            'w',
            '^',
            ' ',
            '^a^'
        ]

        not_palindromes = [
            'moma',
            'race carr',
            '!r a^c e  ca *(r*s&',
            ' ',
            'www.com',
            'a^^w'
        ]

        for palindrome in palindromes:
            self.assertTrue(is_palindrome(palindrome), 'False Positive.')
        for not_palindrome in not_palindromes:
            self.assertFalse(is_palindrome(not_palindrome), 'True Negative')

    def test_odd_even_bit_swap(self):
        self.assertEqual(43, odd_even_bit_swap(23))
        self.assertEqual(1, odd_even_bit_swap(2))
        self.assertEqual(143, odd_even_bit_swap(79))
        self.assertEqual(0, odd_even_bit_swap(0))
        self.assertEqual(-5, odd_even_bit_swap(-10))

if __name__ == '__main__':
    unittest.main()
