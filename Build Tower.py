
def tower_builder(n_floors):
    tower = []
    n = -1
    for i in range(1, n_floors + 1):
        tower . append("*" * (n+2))
        n += 2
    return tower


print(tower_builder(3))

