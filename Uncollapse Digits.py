
def uncollapse(digits):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    uncollapsed = ""
    x = 0
    for i in range(0, len(digits) + 1):
        num = digits[x:i]
        if num in nums:
            uncollapsed = uncollapsed + num + " "
            x = i
    return uncollapsed.strip()


print(uncollapse("ninethreesixthree"))
