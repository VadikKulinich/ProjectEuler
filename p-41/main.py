from utils.numbers import is_prime_number


def is_pandigital(n):
    digits = set()
    size = 0
    while n > 0:
        digits.add(n % 10)
        n = n // 10
        size += 1

    if size != len(digits):
        return False
    for i in range(size):
        if (i + 1) not in digits:
            return False
    return True


def find_largest_pandigital_prime():
    for i in range(10 ** 7 - 1, 1, -1):
        if is_pandigital(i) and is_prime_number(i):
            return i

    return -1


if __name__ == '__main__':
    print(find_largest_pandigital_prime())
