def anagrams(word, words):
    return [sub for sub in words if sorted(sub) == sorted(word)]


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
