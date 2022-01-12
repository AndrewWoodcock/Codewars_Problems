
def make_readable(seconds):
    hours = str(seconds / 3600)[:2]
    rem = str(seconds / 3600)[2:]
    print(rem)


print(make_readable(86399))
print(make_readable(125))
