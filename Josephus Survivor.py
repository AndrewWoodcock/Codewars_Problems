

def josephus_survivor(n, k):
    circle = list(range(1, n + 1))

    cnt = 1
    i = 0
    while len(circle) > 1:
        person = circle[i]
        if i + 1 > len(circle):
            i = 0
        else:
            i += 1


    return circle






print(josephus_survivor(7, 3))

