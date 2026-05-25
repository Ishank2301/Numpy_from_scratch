import numpy as np


def show(label, value):
    print(f"{label}: {value}")


def main():
    numbers = np.array([1, 2, 3])
    show("squares", numbers**2)

    decimals = np.array([1.7, 3.0, 4.9, 5.6])
    show("rounded", np.round(decimals))
    show("floor", np.floor(decimals))
    show("ceil", np.ceil(decimals))
    show("pi", np.pi)

    radii = np.array([1, 2, 3])
    show("circle areas", np.pi * radii**2)

    left = np.array([1, 2, 3])
    right = np.array([4, 8, 9])
    show("add", left + right)
    show("power", left**right)
    show("multiply", left * right)
    show("divide", left / right)

    scores = np.array([91, 92, 33, 67, 75, 22])
    show("equals 22", scores == 22)
    show("less than or equal to 60", scores <= 60)
    show("less than or equal to 33", scores <= 33)

    passed_scores = scores.copy()
    passed_scores[passed_scores < 60] = 0
    show("scores below 60 set to 0", passed_scores)


if __name__ == "__main__":
    main()
