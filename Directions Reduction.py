
def reduce(arr: list, direc: dict) -> list:
    for i in range(0, len(arr)):
        if (i+1 <= (len(arr)-1)) and (arr[i+1] == direc[arr[i]]):
            arr.pop(i)
            arr.pop(i)
            return reduce(arr, direc)
    return arr


def dirReduc(arr: list):
    dir_dict = {"NORTH": "SOUTH",
                "SOUTH": "NORTH",
                "EAST": "WEST",
                "WEST": "EAST"}

    return reduce(arr, dir_dict)


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))



