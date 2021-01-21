
def increment_string(strng):
    strng = strng.strip()
    if (strng == "") or (strng is None):
        return "1"
    num = ""
    # get number if present
    no_digit = False
    i = len(strng) - 1
    while no_digit is False:
        if strng[i].isdigit():
            num = num + strng[i]
            i -= 1
        else:
            no_digit = True
    num = num[::-1]
    if num == "":
        return strng + "1"
    else:
        strng = strng.replace(num, "")
        length = len(num)
        num_int = int(num)
        num_int += 1
        num_str = str(num_int)
        if len(num_str) < length:
            dif = length - len(num_str)
            return strng + ("0" * dif) + num_str
        else:
            return strng + num_str



print(increment_string("foobar99"))
print(increment_string("foobar099"))
print(increment_string("foobar00"))
print(increment_string(""))
