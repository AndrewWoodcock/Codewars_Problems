

def find_even_index(arr):
    for i in range(0, len(arr)):
        left = arr[:i]
        right = arr[i+1:]
        if sum(left) == sum(right):
            return i
    return -1


print(find_even_index([1, 2, 3, 4, 3, 2, 1]))
print(find_even_index([20, 10, -80, 10, 10, 15, 35]))
