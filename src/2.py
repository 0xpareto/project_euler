"""
Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose 
values do not exceed four million, find the sum of the even-valued terms.

"""


def main() -> int:
    x: int = 1
    y: int = 2

    all_fibs: list = [x, y]
    while y <= 4000000:
        y_prime = y
        y = x + y
        x = y_prime
        all_fibs.append(y)

    return sum([x for x in all_fibs if x % 2 == 0])


if __name__ == "__main__":
    result = main()
    print(result)
