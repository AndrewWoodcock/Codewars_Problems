# https://www.codewars.com/kata/56b8903933dbe5831e000c76/train/python

def spoonerize(words):
    wrds = words.split()
    x, y = wrds[0][0], wrds[1][0]
    return y + wrds[0][1:] + " " + x + wrds[1][1:]


print(spoonerize("nit picking"))
