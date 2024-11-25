import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as f:
        reader = csv.DictReader(f)
        lines = [OrderedDict(row) for row in reader]

    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(lines, f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
