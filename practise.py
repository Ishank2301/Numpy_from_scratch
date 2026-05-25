numbers = [1, 2, 3, 4, 5, 6, 7]


def main():
    print(f"last three reversed: {numbers[-3:][::-1]}")
    print(f"from fourth-last backwards: {numbers[-4::-1]}")


if __name__ == "__main__":
    main()
