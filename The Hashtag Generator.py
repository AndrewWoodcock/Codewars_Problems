

def generate_hashtag(s):
    s = "#" + s.strip().title().replace(" ", "")
    if (len(s) > 140) or s == "#":
        return False
    else:
        return s


print(generate_hashtag(" Hello there thanks for trying my Kata"))
print(generate_hashtag("c i n"))
print(generate_hashtag(""))
