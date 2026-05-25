import numpy as np


def show(label, value):
    print(f"{label}: {value}")


def main():
    numbers = np.array([1, 2, 3, 4, 5, 7])
    show("original", numbers)

    numbers = np.insert(numbers, 0, 4)
    show("insert 4 at index 0", numbers)

    numbers = np.append(numbers, 4)
    show("append 4", numbers)

    numbers = np.delete(numbers, 4)
    show("delete index 4", numbers)

    doubled = numbers * 2
    show("multiply by 2", doubled)
    show("array type", type(doubled).__name__)

    shifted = doubled + 3
    show("add 3", shifted)

    combined = shifted + shifted
    show("add array to itself", combined)

    incremented = combined + 1
    show("add 1", incremented)

    minus_two = incremented - 2
    show("subtract 2", minus_two)

    quotient = minus_two // 2
    show("floor divide by 2", quotient)

    half = quotient / 2
    show("true divide by 2", half)


if __name__ == "__main__":
    main()
