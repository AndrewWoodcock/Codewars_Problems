

def div_con(x):
    string_ints = 0
    int_ints = 0

    for item in x:
        if type(item) == str:
            string_ints += int(item)
        elif type(item) == int:
            int_ints += item

    return int_ints - string_ints


print(div_con(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0']))
