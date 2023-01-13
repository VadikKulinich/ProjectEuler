from math import factorial


def factorial_sum(n):
    n_factorial = factorial(n)
    digit_sum = 0
    while n_factorial > 0:
        digit_sum += n_factorial % 10
        n_factorial = n_factorial // 10
    return digit_sum


if __name__ == '__main__':
    print(factorial_sum(100))
