import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$"
    return re.match(pattern, ip) is not None


if __name__ == "__main__":
    main()