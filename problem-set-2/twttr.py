text = input("Digite algo :")

def remove_vogais(str):

    vogais = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")

    for c in str:

        if c in vogais:

            str = str.replace(c, "")

    return str


print(remove_vogais(text))


