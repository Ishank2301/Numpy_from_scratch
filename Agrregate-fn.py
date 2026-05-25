import numpy as np


def show(label, value):
    print(f"{label}: {value}")


def main():
    scores = np.array(
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
        ]
    )

    show("array", scores)
    show("sum", np.sum(scores))
    show("mean", np.mean(scores))
    show("standard deviation", np.std(scores))
    show("variance", np.var(scores))
    show("minimum", np.min(scores))
    show("maximum", np.max(scores))
    show("index of minimum", np.argmin(scores))
    show("index of maximum", np.argmax(scores))
    show("column sums", np.sum(scores, axis=0))
    show("row sums", np.sum(scores, axis=1))


if __name__ == "__main__":
    main()
