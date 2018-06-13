# import ...


# -----------------------------------------------------------------------------
# Exercise (Medium): Nested For-Loops

# Create the following pattern using nested for-loops.
# Return the result as a string with a newline at the end.
# Note) Ignore the left line of python comments (#).
#       The patten to make is the box.

#   ##########
#   ##      ##
#   # #    # #
#   #  #  #  #
#   #   ##   #
#   #   ##   #
#   #  #  #  #
#   # #    # #
#   ##      ##
#   ##########

# Hint(s): There are two (or more) viable methods to solve this.
# Try to come up with both. The first method involves
# printing the first and last line outside of the loop,
# or adding an if statement for the first and last line
# in the loop. The second method involves an if statement
# with multiple (~6) conditions separated with an OR clause,
# but with this method, no separate print statements are needed
# for the first and last line because you can merge them in
# with the large if statement inside the loops.
# -----------------------------------------------------------------------------
def pound_pattern():
    return ""


# -----------------------------------------------------------------------------
# Exercise (Medium): Reverse Half a Linked-List

# Your function will be given the head of a linked list.
# What you want to do is return the head of the linked list,
# but with the second half of the linked list reversed.

# Ex) 1->2->3->4->5->None returns 1->2->3->5->4->None
#     1->2->3->4->5->6->None returns 1->2->3->6->5->4->None
# -----------------------------------------------------------------------------
def reverse_second_half_linked_list(head = None):
    return None


class Node:

    def __init__(self, next_node = None, value = 0):
        if next_node is None:
            self.next = Node()
        else:
            self.next = next_node

        self.value = value


# -----------------------------------------------------------------------------
# Exercise (medium): Alien Language

# Given a SORTED dictionary of an alien language having N
# words and k starting alphabets of standard dictionary
# the task is to complete the function which returns a
# string denoting the order of characters in the language.

# Examples:
# Input: dictionary = [ "baa", "abcd", "abca", "cab", "cad" ]
# k = 4
# Output: "bdac"
# Input: dictionary = [ "caa", "aaa", "aab" ]
# k = 3
# Output: "cab"

# Tips: For the first example, you know that 'b' is the
# first letter in the alien language because the
# first word starts with 'b'. You then know 'a'
# is the second because the second/third words
# start with 'a'. You also know that 'c' is the
# third letter since the last two words start with
# 'c'. You know that 'd' is ahead of 'a' though because
# the second word 'abcd' is ahead of 'abca' and you
# also know that 'd' is behind 'b' since 'cab' is
# ahead of 'cad'. This tells you that b>d>a>c.
# For the second example, you know that 'c' is the
# first letter in the alien language because the
# first word starts with 'c'.
# To find the second letter, you look at the second word
# which is 'aaa.' This tells you 'a' is the second letter.
# You still don't know the third letter so you go to the next
# word which has 'b' in it so you now know 'b' will be
# the third and final (because k = 3) letter.
# -----------------------------------------------------------------------------
def alien_language(words = None):
    return ""


# -----------------------------------------------------------------------------
# Exercise (Medium): Greatest Common Denominator
#
# Return the greatest common denominator between two integers.
# The inputs may be negative values, but the return must not be negative.
# Brush up on how to find GCDs if the following examples do not make sense.
#
# gcd(5, 15) = 5
# gcd(0, 0) = 0
# gcd(0, 1) = 1
# gcd(-2, -2) = 2
# gcd(-2, 2) = 1
# -----------------------------------------------------------------------------
def greatest_common_denominator(a=0, b=0):
    return 0
