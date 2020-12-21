

def max_sequence(arr):
    max_so_far = 0
    max_ending = 0
    for i in range(0, len(arr)):
        max_ending = max_ending + arr[i]
        if max_so_far < max_ending:
            max_so_far = max_ending
        if max_ending < 0:
            max_ending = 0
    return max_so_far


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
