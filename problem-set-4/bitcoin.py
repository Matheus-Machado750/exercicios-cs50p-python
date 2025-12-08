import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        price = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")

    total = bitcoins * price
    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()

#Obtive ajuda do ChatGPT para me ajudar com esse exercício
