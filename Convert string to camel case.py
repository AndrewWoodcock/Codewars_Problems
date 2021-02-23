

def to_camel_case(text):
    if text == "":
        return ""
    split = text.replace("_", "-")
    split = split.split("-")

    for i in range(0, len(split)):
        if i == 0:
            pass
        else:
            split[i] = split[i].capitalize()
    return "".join(split)


print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("A_cat-Was_cute"))
