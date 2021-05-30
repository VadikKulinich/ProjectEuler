import math


def is_prime_number(number):
    if number < 2:
        return False
    for i in range(2, int_sqrt(number) + 1):
        if number % i == 0:
            return False
    return True


def reverse_number(n):
    reversed_number = 0
    number = n
    while number > 0:
        reversed_number = reversed_number * 10 + number % 10
        number = number // 10
    return math.copysign(reversed_number, n)


def int_sqrt(number):
    return int(math.sqrt(number))
