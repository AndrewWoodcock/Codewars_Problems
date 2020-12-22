
def pig_it(text: str) -> str:
    word_list = [word for word in text.split()]
    return " ".join([word[1:] + word[:1] + "ay" if word.isalpha() else word for word in word_list])


print(pig_it("Quis custodiet ipsos custodes ?"))
