"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def is_prime(x: int):
    if x % 2 == 0:
        return False
    for _ in range(2, x):
        if not x % _:
            return False
    return True


def main() -> int:
    primes: list = [2]
    x: int = 3
    while len(primes) < 10001:
        if is_prime(x):
            primes.append(x)
        x += 1
    return primes[-1]


if __name__ == "__main__":
    result = main()
    print(result)
