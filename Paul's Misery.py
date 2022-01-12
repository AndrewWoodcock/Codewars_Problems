

def paul(x: list) -> str:
    scores = {'kata': 5,
              'Petes kata': 10,
              'life': 0,
              'eating': 1}

    score_sum = sum([scores[val] for val in x])
    if score_sum < 40:
        return 'Super happy!'
    elif score_sum < 70:
        return 'Happy!'
    elif score_sum < 100:
        return 'Sad!'
    else:
        return 'Miserable!'


def main():
    print(paul(['life', 'eating', 'life']))
    print(paul(['Petes kata', 'Petes kata', 'eating', 'Petes kata', 'Petes kata', 'eating']))


if __name__ == '__main__':
    main()

