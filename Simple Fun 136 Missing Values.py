def missing_values(seq):
    freqs = {}
    x, y = 0, 0
    for el in seq:
        if el not in freqs:
            freqs[el] = 1
        else:
            freqs[el] += 1

    for key, value in freqs.items():
        if value == 1:
            x = key
        elif value == 2:
            y = key

    return x * x * y


print(missing_values([1, 1, 1, 2, 2, 3]))
