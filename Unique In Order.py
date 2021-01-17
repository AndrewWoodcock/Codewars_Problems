

def unique_in_order(iterable):
    curr = None
    unique_order = []
    for i in range(0, len(iterable)):
        if curr != iterable[i]:
            curr = iterable[i]
            unique_order.append(iterable[i])
    return unique_order


print(unique_in_order('ABBCcAD'))
