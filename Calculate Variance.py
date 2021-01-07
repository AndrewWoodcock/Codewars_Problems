

def variance(numbers):
    mean = sum(numbers) / len(numbers)
    results = [((num - mean) ** 2) for num in numbers]
    return sum(results) / len(results)


print(variance([1, 2, 2, 3]))
