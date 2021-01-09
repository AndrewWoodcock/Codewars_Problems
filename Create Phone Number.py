
def create_phone_number(n):
    n = "".join([str(num) for num in n])
    return "(" + n[:3] + ")" + " " + n[3:6] + "-" + n[6:]


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
