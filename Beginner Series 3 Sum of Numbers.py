

def get_sum(a, b):
    my_sum = 0
    for i in range(min(a, b), max(a, b) + 1):
        my_sum += i
    return my_sum


print(get_sum(-1, 2))
