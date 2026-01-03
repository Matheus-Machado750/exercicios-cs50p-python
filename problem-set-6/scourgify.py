import sys
import csv


def main():
    # Verifica argumentos
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, newline="") as infile:
            reader = csv.DictReader(infile)

            with open(output_file, "w", newline="") as outfile:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    last, first = row["name"].split(", ")
                    writer.writerow({
                        "first": first,
                        "last": last,
                        "house": row["house"]
                    })

    except FileNotFoundError:
        sys.exit("Could not read input file")


if __name__ == "__main__":
    main()