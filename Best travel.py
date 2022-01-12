
from itertools import permutations


# xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
xs = [50, 55, 57, 58, 60]


def sub_array_sum(sub_array, t):
    return True if sum(sub_array) <= t else False


def choose_best_sum(t, k, ls):
    permutes = list(permutations(ls, k))
    possible = [sum(perm) for perm in permutes if sub_array_sum(perm, t)]
    print(sorted(possible, reverse=True)[0])





# print(choose_best_sum(230, 4, xs))
print(choose_best_sum(174, 3, xs))