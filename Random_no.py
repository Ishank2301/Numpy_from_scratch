import numpy as np


def show(label, value):
    print(f"{label}: {value}")


def main():
    rng = np.random.default_rng(seed=2026)

    show("dice rolls", rng.integers(low=1, high=7, size=(3, 2)))
    show("random floats", rng.uniform(low=-1, high=1, size=3))

    numbers = np.array([1, 2, 3, 4, 5])
    rng.shuffle(numbers)
    show("shuffled numbers", numbers)

    fruits = np.array(["apple", "banana", "orange", "coconut", "pineapple"])
    choices = rng.choice(fruits, size=(3, 4))
    show("fruit choices", choices)


if __name__ == "__main__":
    main()
