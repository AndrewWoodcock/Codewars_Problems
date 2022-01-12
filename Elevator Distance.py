
def elevator_distance(array):
    dist = 0
    for a, b in zip(array, array[1:]):
        print(a)
        print(b)
        dist += abs(a - b)
    return dist


print(elevator_distance([5, 2, 8]))
