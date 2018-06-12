import unittest
import random

from src.hard_questions import encode_bit, decode_bit_sequence


class HardQuestionsTests(unittest.TestCase):

    def test_error_correction(self):
        accuracy = 0.99         # 99% accuracy required to pass the test
        noise_ratio = 50        # 1 out of 50 bits are flipped
        number_of_inputs = 50   # 50 tests to run

        random.seed()
        input_values = [random.randint(0, 1) for _ in range(number_of_inputs)]
        encoded_input = [encode_bit(bit) for bit in input_values]

        for i in range(len(encoded_input)):
            for j in range(len(encoded_input[i])):
                if random.randint() % noise_ratio == 0:
                    encoded_input[i][j] = ~encoded_input[i][j]

        output_values = [
            decode_bit_sequence(sequence) for sequence in encoded_input
        ]

        max_errors = (1.0 - accuracy) * number_of_inputs
        max_errors = int(max_errors)
        actual_errors = int(number_of_inputs)

        for i in range(number_of_inputs):
            if input_values[i] != output_values[i]:
                actual_errors -= 1

        message = "Error too large, " + str(max_errors) + " was expected but"
        message += " the actual error count was " + str(actual_errors)
        self.assertTrue(actual_errors <= max_errors, message)


if __name__ == '__main__':
    unittest.main()
