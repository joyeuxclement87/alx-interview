#!/usr/bin/python3
"""Working on UTF-8 Validation"""


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    num_byte = 0

    m_1 = 1 << 7
    m_2 = 1 << 6

    for a in data:

        m_byte = 1 << 7

        if num_byte == 0:

            while m_byte & a:
                num_byte += 1
                m_byte = m_byte >> 1

            if num_byte == 0:
                continue

            if num_byte == 1 or num_byte > 4:
                return False

        else:
            if not (a & m_1 and not (a & m_2)):
                return False

        num_byte -= 1

    return num_byte == 0
