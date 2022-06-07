"""
Even Fibonacci numbers
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""


def main():
    n: int = 600851475143

    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return max(factors)


if __name__ == "__main__":
    result = main()
    print(result)
