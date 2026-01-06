from datetime import date
import inflect
import sys


p = inflect.engine()


def main():
    birth = input("Date of Birth: ")
    try:
        minutes = minutes_since_birth(birth)
    except ValueError:
        sys.exit("Invalid date")

    print(p.number_to_words(minutes, andword="").capitalize() + " minutes")


def minutes_since_birth(birthdate):
    try:
        year, month, day = map(int, birthdate.split("-"))
        birth = date(year, month, day)
    except Exception:
        raise ValueError

    today = date.today()
    if birth > today:
        raise ValueError

    delta = today - birth
    return delta.days * 24 * 60


if __name__ == "__main__":
    main()
