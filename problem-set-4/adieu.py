names = []

while True:
    try:
        name = input()
        names.append(name)

    except EOFError:
        break

if len(names) == 1:
    farewell = names[0]

elif len(names) == 2:
    farewell = " and ".join(names)

else:
    farewell = ", ".join(names[:-1]) + ", and " + names[-1]

print(f"Adieu, adieu, to {farewell}")

#Tive ajuda do ChatGPT para me guiar
