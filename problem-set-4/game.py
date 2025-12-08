import random

def main():

    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            pass

    # Gerar número aleatório
    number = random.randint(1, level)

    # Loop
    while True:
        try:
            guess = int(input("Guess: "))

            if guess <= 0:
                continue

            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                print("Just right!")
                break

        except ValueError:
            pass

main()

#Tive ajuda do ChatGPT com alguns erros de lógica do meu código
