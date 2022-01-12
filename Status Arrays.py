
import numpy as np


def status(nums):
    stat_dict = {}
    for i in enumerate(nums):
        x = np.array([nums])
        less_than = len(x[x < i[1]])
        stat_dict[i[1]] = i[0] + less_than
        print(i[0] + less_than)

    # return stat_dict





print(status([6, 9, 3, 8, 2, 3, 1]))
