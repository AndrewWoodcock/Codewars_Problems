

class Weight:

    def __init__(self, weight):
        self.weight = weight
        self.number = num_words[int(str(weight[0][0]))]


num_words = {1: "one",
             2: "two",
             3: "three",
             4: "four",
             5: "five",
             6: "six",
             7: "seven",
             8: "eight",
             9: "nine"}


def split_input(string: str) -> list:
    return string.split()


def sum_weight(weight: str) -> int:
    return sum([int(char) for char in weight])


def get_alpha(number: int):
    number = str(number)
    return [num_words[int(number[0])]]


def order_weight(strng):
    weight_list = split_input(strng)
    weighted_weights = []
    for element in weight_list:
        weighted_weights.append((element, sum_weight(element)))

    sorted_weights = sorted(weighted_weights, key=lambda tup: tup[1])

    re_sorted = sorted([Weight(element) for element in sorted_weights], key=lambda weight: weight.number)
    for element in re_sorted:
        print(element.weight)


# print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))


def order_weight(strng):
    weight_weights = {}
    weights = strng.strip().split()
    for weight in weights:
        digits = [int(num) for num in weight]
        new_weight = sum(digits)
        weight_weights[weight] = new_weight

    re_ordered = dict(sorted(weight_weights.items(), key=lambda item: item[1]))
    new_list = ""
    for key, value in re_ordered.items():
        new_list = new_list + " " + key
    return new_list.strip()


print(order_weight("103 123 4444 99 2000"))
