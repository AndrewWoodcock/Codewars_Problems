
import itertools


def next_bigger(n):
    num_str = [char for char in str(n)]
    perms = list(itertools.permutations(num_str))
    num_perms = sorted([int("".join(perm)) for perm in perms])
    print(num_perms)

    if (num_perms.index(n) + 1 > len(num_perms)) or (num_perms.index(n) + 2 > len(num_perms)):
        return -1
    if num_perms[num_perms.index(n) + 1] == n:
        return num_perms[num_perms.index(n) + 2]
    else:
        return num_perms[num_perms.index(n) + 1]


print(next_bigger(2017))
print(next_bigger(414))
