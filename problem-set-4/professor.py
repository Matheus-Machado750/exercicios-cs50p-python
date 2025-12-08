import random as rd

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y

        tries = 0

        while tries < 3:
            try:
                answer = int(input(f"{x} + {y} = "))

                if answer == correct:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1

            except ValueError:
                print("EEE")
                tries += 1

        if tries == 3:
            print(f"{x} + {y} = {correct}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if level in [1, 2, 3]:
                return level

        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return rd.randint(0, 9)

    elif level == 2:
        return rd.randint(10, 99)

    else:
        return rd.randint(100, 999)


if __name__ == "__main__":
    main()

#Tive ajuda do ChatGPT para idealizar o código e corrigir bugs
