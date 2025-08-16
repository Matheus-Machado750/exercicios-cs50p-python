def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False

    if not s[:2].isalpha():
        return False

    for i in range(2, len(s)):
        if s[i].isdigit():

            if s[i] == "0":
                return False

            # Checa se todo resto são dígitos
            if not s[i:].isdigit():
                return False

            break  # achou números e são válidos, sai do loop

    return True


main()

# Utilizei a ajuda do ChatGPT para aplicar o Slicing, colocar um break no for e usar o "if not" ao invés de só "if"
