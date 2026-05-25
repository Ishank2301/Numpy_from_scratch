import numpy as np


def show(label, value):
    print(f"{label}: {value}")


def main():
    letters = np.array(
        [
            [["A", "B", "C"], ["D", "E", "F"], ["J", "H", "I"]],
            [["K", "L", "M"], ["N", "O", "P"], ["Q", "R", "S"]],
            [["T", "U", "V"], ["W", "X", "Y"], ["J", "Z", ""]],
        ]
    )

    show("dimensions", letters.ndim)
    show("chain indexing", letters[0][0][0])
    show("multidimensional indexing", letters[2, 2, 1])

    word = letters[0, 1, 0] + letters[0, 0, 0] + letters[2, 0, 0] + letters[0, 0, 0]
    show("built word", word)

    scores = np.array([1, 5, 7, 9, 3, 4, 5, 5, 6])
    show("skip first", scores[1:])
    show("last item as slice", scores[-1:])
    show("last five except final", scores[-5:-1])
    show("drop last", scores[:-1])
    show("every second item from 1 to 8", scores[1:8:2])
    show("middle section", scores[1:-4])
    show("reverse", scores[::-1])

    grid = np.array(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 0, 1, 2],
            [4, 6, 9, 3],
        ]
    )

    show("last row", grid[-1:])
    show("all except last row", grid[:-1])
    show("first row plus last row", grid[0:1] + grid[-1:])
    show("single item", grid[0, 0])
    show("last column", grid[:, -1])
    show("first two rows and columns", grid[0:2, :-2])
    show("rows reversed", grid[::-1])
    show("inner square", grid[1:-1, 1:-1])
    show("bottom-right block reversed", grid[2:, -2:][::-1])


if __name__ == "__main__":
    main()
