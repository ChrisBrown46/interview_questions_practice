# import ...


# -----------------------------------------------------------------------------
# Exercise (Very-Hard): Error Correction

# You will be given a bit (0 or 1) represented by a boolean value (bit).
# You must encode this bit as a bit sequence (list of bools or numbers)
# so that when noise is introduced you will be able to decode the string
# and regain your original bit that was encoded. Noise in this case will
# be represented by random bit flips in any sequence generated by encode_bit.
# Currently you must achieve an accuracy of 99% when there is a noise
# ratio of 1/50 bits flipped. These values may be changed in the unit
# tests if it is too aggressive and difficult to solve.

# The idea behind this is...
#   Original Bit ->
#       encodeBit ->
#           Noise Introduced ->
#       decodeBitSequence ->
#   Original Bit
# -----------------------------------------------------------------------------
def encode_bit(bit = False):
    return [0 for _ in range(100)]


def decode_bit_sequence(encoded_bit_sequence = None):
    return False