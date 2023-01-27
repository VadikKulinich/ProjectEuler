from math import factorial


def digit_factorials():
    total_sum = 0
    for i in range(10, 1854721):
        if i == sum_of_factorials(i):
            total_sum += i

    return total_sum


def sum_of_factorials(n):
    sum = 0
    while n > 0:
        sum += factorial(n % 10)
        n = n // 10

    return sum


if __name__ == '__main__':
    print(digit_factorials())
