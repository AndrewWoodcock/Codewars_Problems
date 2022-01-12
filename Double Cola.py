from collections import deque

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]


def who_is_next(names, r):
    queue = deque(names)
    print(list(queue))
    for i in range(1, r):
        queue.append(queue[0])
        queue.append(queue[0])
        del queue[0]
        print(list(queue))
    return list(queue)[0]




print(who_is_next(names, 3))
