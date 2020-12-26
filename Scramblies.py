# Checking if string 2 can be made from string 1

from collections import Counter


def scramble(s1, s2):
    s1set = Counter(s1)
    return all(count <= s1set[c] for c, count in Counter(s2).items())


print(scramble("rkqodlw", "world"))
