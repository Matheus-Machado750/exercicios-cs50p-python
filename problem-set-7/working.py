import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::([0-5]\d))? (AM|PM) to (\d{1,2})(?::([0-5]\d))? (AM|PM)$"
    match = re.match(pattern, s)

    if not match:
        raise ValueError

    h1, m1, p1, h2, m2, p2 = match.groups()

    h1 = int(h1)
    h2 = int(h2)
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0

    if not (1 <= h1 <= 12 and 1 <= h2 <= 12):
        raise ValueError

    start = to_24h(h1, m1, p1)
    end = to_24h(h2, m2, p2)

    return f"{start} to {end}"


def to_24h(hour, minute, period):
    if period == "AM":
        hour = 0 if hour == 12 else hour
    else:
        hour = 12 if hour == 12 else hour + 12

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()