import unittest

from src.medium_questions import pound_pattern
from src.medium_questions import reverse_second_half_linked_list, Node
from src.medium_questions import alien_language
from src.medium_questions import greatest_common_denominator


class MediumQuestionsTests(unittest.TestCase):

    def test_pound_pattern(self):
        expected = (
            '##########\n'
            '##      ##\n'
            '# #    # #\n'
            '#  #  #  #\n'
            '#   ##   #\n'
            '#   ##   #\n'
            '#  #  #  #\n'
            '# #    # #\n'
            '##      ##\n'
            '##########\n'
        )

        self.assertEqual(expected, pound_pattern())

    def test_reverse_second_half_linked_list(self):
        # Start head of list with value 1
        head = Node(value = 1)

        # Create linked list with values: 1->2->3->4->5->None
        traversal_node = head
        for i in range(2, 6):
            next_node = Node(value = i)
            traversal_node.next = next_node
            traversal_node = traversal_node.next
        traversal_node.next = None

        # Call function to test
        head = reverse_second_half_linked_list(head)

        # Verify the second half (4/5) have swapped
        for i in range(1, 4):
            self.assertEqual(i, head.value)
            head = head.next
        for i in range(5, 3, -1):
            self.assertEqual(i, head.value)
            head = head.next

        # Same idea but with a list of 1 through 6
        head = Node(value = 1)

        traversal_node = head
        for i in range(2, 7):
            next_node = Node(value = i)
            traversal_node.next = next_node
            traversal_node = traversal_node.next
        traversal_node.next = None

        head = reverse_second_half_linked_list(head)

        for i in range(1, 4):
            self.assertEqual(i, head.value)
            head = head.next
        for i in range(6, 3, -1):
            self.assertEqual(i, head.value)
            head = head.next

        # Edge Case Testing
        head = Node(value = 1)
        head = reverse_second_half_linked_list(head)
        self.assertEqual(1, head.value)

        head = None
        head = reverse_second_half_linked_list(head)
        self.assertIsNone(head)

    def test_alien_language(self):
        first_language = [
            'baa', 'abcd', 'abca', 'cab', 'cad'
        ]

        second_language = [
            'caa', 'aaa', 'aab'
        ]

        edge_case_1 = ['abc']
        edge_case_2 = ['']
        edge_case_3 = []

        self.assertEqual('bdac', alien_language(first_language))
        self.assertEqual('cab', alien_language(second_language))
        self.assertEqual('abc', alien_language(edge_case_1))
        self.assertEqual('', alien_language(edge_case_2))
        self.assertEqual('', alien_language(edge_case_3))

    def test_greatest_common_denominator(self):
        self.assertEqual(0, greatest_common_denominator(0, 0))
        self.assertEqual(1, greatest_common_denominator(0, 1))
        self.assertEqual(5, greatest_common_denominator(5, 15))
        self.assertEqual(2, greatest_common_denominator(-2, -2))
        self.assertEqual(1, greatest_common_denominator(-2, 5))
        self.assertEqual(21, greatest_common_denominator(958839, 593082))
        self.assertEqual(3, greatest_common_denominator(
            9859378098709875378, 598537109873209875))

if __name__ == '__main__':
    unittest.main()
