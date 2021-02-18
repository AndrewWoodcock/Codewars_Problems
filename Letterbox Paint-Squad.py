

def paint_letterboxes(start, finish):
    nums = {0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0}

    for i in range(start, finish + 1):
        split = [int(d) for d in str(i)]
        for digit in split:
            nums[digit] += 1

    out = []
    for key, value in nums.items():
        out.append(value)
    return out


print(paint_letterboxes(125, 132))
