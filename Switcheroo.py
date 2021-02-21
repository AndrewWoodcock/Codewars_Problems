
def switcheroo(string):
    out = []
    for char in string:
        if char == "a":
            out.append("b")
        elif char =="b":
            out.append("a")
        else:
            out.append("c")
    return "".join(out)


print(switcheroo("aaabcccbaaa"))
