
def odd_or_even(arr):
    summed = sum(arr)
    if summed % 2 != 0:
        return "odd"
    else:
        return "even"


print(odd_or_even([0, 1, 3]))
