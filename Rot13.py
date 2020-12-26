
import string
from collections import deque


def rot13(message):
    alphabet = deque(string.ascii_lowercase)
    new_str = ""
    for element in message:
        if element.isalpha():
            char = element.lower()
            # rotate deque until char is element 0
            while alphabet[0] != char:
                alphabet.rotate(1)
            # get 13 chars after char
            plus_thirteen = alphabet[13]
            if element.isupper():
                plus_thirteen = plus_thirteen.upper()
            new_str = new_str + plus_thirteen
        else:
            new_str = new_str + element

    return new_str


rot13("Test")
