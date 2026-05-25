import numpy as np


def show(label, value):
    print(f"{label}: {value}")


def main():
    # Broadcasting works when matching dimensions are equal or one of them is 1.
    row = np.array([1, 2, 3])
    column = np.array([[1], [2], [3], [4]])

    show("row shape", row.shape)
    show("column shape", column.shape)
    show("row * column", row * column)

    wide_row = np.array([[1, 2, 3, 6, 7, 8, 9, 10]])
    tall_column = np.arange(1, 11).reshape(10, 1)

    show("wide row shape", wide_row.shape)
    show("tall column shape", tall_column.shape)
    show("broadcasted product", wide_row * tall_column)


if __name__ == "__main__":
    main()
