
vowels = ["a", "e", "i", "o", "u"]

def get_count(input_str):
    num_vowels = 0
    for char in input_str:
        if char.lower() in vowels:
            num_vowels += 1
    return num_vowels


print(get_count("abracadabra"))