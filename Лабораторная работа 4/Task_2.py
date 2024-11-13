import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as file:
        reader_csv = csv.DictReader(file)
        rows = [row for row in reader_csv]

    with open(OUTPUT_FILENAME, 'w') as file:
        json.dump(rows, file, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
