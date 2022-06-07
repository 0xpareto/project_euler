"""
A palindromic number reads the same both ways. The largest palindrome made from the product of 
two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def main() -> int:
    largest: int = 0
    for i in range(1000):
        for j in range(1000):
            n = str(i * j)
            if n == n[::-1]:
                largest = max(int(n), largest)

    return largest


if __name__ == "__main__":
    result = main()
    print(result)
