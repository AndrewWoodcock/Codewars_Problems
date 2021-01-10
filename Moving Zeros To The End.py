
def move_zeros(array, cnt=0):

    while cnt <= len(array):
        if not array:
            return array
        cnt += 1
        for e in enumerate(array):
            if ((e[1] == 0) or (e[1] == 0.0)) and e[1] is not False:
                array.append(array.pop(e[0]))
                cnt += 1
                return move_zeros(array, cnt)
    return array


print(move_zeros(['y', 0, 0, -1, 4, 'string', 2, False, True, 'y', 'c', True, -4, -3, 0, 0, 9, 0, 'z', -4, -3, '0',
                  -4, True, 0, '0', 0, 0, 7, 'x', 4, 0, 3, 0]))
