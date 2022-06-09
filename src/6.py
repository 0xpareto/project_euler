"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""


def main() -> int:
    return sum([x for x in range(101)]) ** 2 - sum([x ** 2 for x in range(101)])


if __name__ == "__main__":
    result = main()
    print(result)
