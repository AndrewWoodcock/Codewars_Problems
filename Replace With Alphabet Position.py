
import string


def alphabet_hash():
    alphabet = list(string.ascii_lowercase)
    alpha_dict = {}
    for element in enumerate(alphabet):
        alpha_dict[element[1]] = str(element[0] + 1)
    return alpha_dict


def alphabet_position(text):
    out_str = ""
    alpha_dict = alphabet_hash()
    for char in text:
        if char.isalpha():
            out_str = out_str + " " + alpha_dict[char.lower()]
    return out_str.strip()


print(alphabet_position("The sunset sets at twelve o' clock."))
