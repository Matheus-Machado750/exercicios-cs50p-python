case = input("Insert your name : ")

def case_transform(name):

    new_name = ""

    for i in name:

        if i.isupper():
            new_name += "_" + i.lower()

        else:
            new_name += i

    return new_name

print(case_transform(case))

# Tive ajuda do ChatGPT para realizar essa atividade sem usar o .replace()
