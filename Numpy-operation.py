def two_sum(arr, target):
    seen = set()

    for number in arr:
        complement = target - number
        if complement in seen:
            return True
        seen.add(number)

    return False


def main():
    numbers = [2, 3, 4, 7, 9, 0]
    target = 9
    print(f"has pair for {target}: {two_sum(numbers, target)}")


if __name__ == "__main__":
    main()
