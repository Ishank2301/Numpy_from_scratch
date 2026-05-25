import numpy as np


def show(label, value):
    print(f"{label}: {value}")


def main():
    ages = np.array(
        [
            [21, 17, 19, 20, 16, 30, 18, 65],
            [39, 22, 15, 99, 18, 19, 20, 21],
        ]
    )

    minors = ages[ages < 18]
    adults = ages[(ages >= 18) & (ages <= 65)]
    seniors = ages[ages > 65]
    evens = ages[ages % 2 == 0]
    odds = ages[ages % 2 != 0]
    labels = np.where(ages >= 18, "adult", "minor")

    show("ages", ages)
    show("senior mask", ages > 65)
    show("minors", minors)
    show("adults", adults)
    show("seniors", seniors)
    show("even ages", evens)
    show("odd ages", odds)
    show("adult/minor labels", labels)


if __name__ == "__main__":
    main()
