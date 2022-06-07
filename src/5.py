"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def divisible1to20(x: int) -> bool:
    # 1-20 can be simplified by removing factors to the following
    for i in [11, 13, 14, 16, 17, 18, 19, 20]:
        if not x % i == 0:
            return False
    return True


def main() -> int:
    n: int = 20
    while True:
        if divisible1to20(n):
            return n
        # Can step 20 at a time as 20 is the largest factor
        n += 20


if __name__ == "__main__":
    result = main()
    print(result)
