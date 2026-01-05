import validators


def main():
    email = input("Email: ").strip()
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
