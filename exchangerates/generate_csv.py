import csv

from data import get_rates


def generate():
    rates = get_rates()

    if rates:
        sample_rate = rates[0]

        header = sample_rate.keys()

        with open("rates.csv", "w", encoding="UTF8", newline="") as f:
            writer = csv.writer(f, delimiter=";")

            # write the header
            writer.writerow(header)

            print([list(rate.values()) for rate in rates])

            # write the data
            writer.writerows([list(rate.values()) for rate in rates])


if __name__ == "__main__":
    generate()
