from collections import Counter


def sum_pairs(ints: list, s: int):
    my_ints = [element for element in ints]
    res_dict = {}
    i = len(ints)
    while ints:
        res = []
        num = ints.pop()
        diff = s - num
        if diff in ints:
            res.append(diff)
            res.append(num)
            dict_id = i + my_ints.index(diff)
            res_dict[dict_id] = res
            i -= 1
    return res_dict[max(res_dict)] if res_dict else None


print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
print(sum_pairs([4, 3, 2, 3, 4], 6))

# https://www.geeksforgeeks.org/python-program-to-find-all-possible-pairs-with-given-sum/
