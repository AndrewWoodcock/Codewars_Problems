
def passer_rating(att, yds, comp, td, ints):
    vals = []
    A = ((comp / att) - 0.3) * 5
    vals.append(A)
    B = ((yds / att) - 3) * 0.25
    vals.append(B)
    C = (td / att) * 20
    vals.append(C)
    D = 2.375 - ((ints / att) * 25)
    vals.append(D)

    for i in range(0, len(vals)):
        if vals[i] > 2.375:
            vals[i] = 2.375
        elif vals[i] < 0:
            vals[i] = 0

    return round((sum(vals) / 6) * 100, 1)


print(passer_rating(432, 3554, 291, 28, 2))


