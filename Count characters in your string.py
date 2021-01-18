import collections


def count(string):
    return collections.Counter(string)


print(count("aba"))
