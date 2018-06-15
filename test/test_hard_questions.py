import unittest
import random
import math

from src.hard_questions import encode_object, decode_bit_sequence
from src.medium_questions import Node


class HardQuestionsTests(unittest.TestCase):

    def test_error_correction(self):
        accuracy = 0.99         # 99% accuracy required to pass the test
        noise_ratio = 10  # 1 out of 50 bits are flipped

        input_values = [
            'Hello',
            Node(),
            15,
            0,
            None,
            [1, 1, 2, 3, 5, 8],
            {'Hello': 15},
            3.141592,
            math.pi,
            'World'
        ]
        encoded_input = [encode_object(bit) for bit in input_values]

        for i in range(len(encoded_input)):
            for j in range(len(encoded_input[i])):
                if random.randint() % noise_ratio == 0:
                    encoded_input[i][j] = ~encoded_input[i][j]

        output_values = [
            decode_bit_sequence(sequence) for sequence in encoded_input
        ]

        max_errors = (1.0 - accuracy) * len(input_values)
        max_errors = int(max_errors)
        actual_errors = int(len(input_values))

        for i in range(len(input_values)):
            if input_values[i] != output_values[i]:
                actual_errors -= 1

        message = "Error too large, " + str(max_errors) + " was expected but"
        message += " the actual error count was " + str(actual_errors)
        self.assertTrue(actual_errors <= max_errors, message)


if __name__ == '__main__':
    unittest.main()
