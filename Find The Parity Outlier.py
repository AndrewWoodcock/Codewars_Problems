

def find_outlier(integers):
    even_odd = [0, 0]
    for i in range(0, 3):
        if integers[i] % 2 == 0:
            even_odd[0] += 1
        else:
            even_odd[1] += 1
    if even_odd[0] > even_odd[1]:
        return (e for e in integers if e % 2 != 0).__next__()
    else:
        return (e for e in integers if e % 2 == 0).__next__()


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
