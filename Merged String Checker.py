

def is_merge(s, part1, part2):
    sort_s = sorted(s)
    full = sorted(part1 + part2)
    if sort_s == full:
        print(list(enumerate(s)))
        print(list(enumerate(part1 + part2)))
        if list(enumerate(s)) == list(enumerate(part1 + part2)):
            return True


print(is_merge('codewars', 'cdw', 'oears'))
print(is_merge('codewars', 'cdwr', 'oeas'))
