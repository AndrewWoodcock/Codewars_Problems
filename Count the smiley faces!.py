


def count_smileys(arr):
    eyes = ":", ";"
    nose = "-", "~"
    mouth = ")", "D"
    valid = 0
    val = 0
    for smiley in arr:
        if smiley[0] in eyes:
            val += 1
        if smiley[1] in nose:
            val += 1
            if smiley[2] in mouth:
                val += 1

                if val == 3:
                    valid += 1
        elif smiley[1] in mouth:
            val += 1

            if val == 2:
                valid += 1
        print(smiley, valid)
    return valid


print(count_smileys([':)', ':(', ':D', ':O', ':;']))
