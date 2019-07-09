import math


def is_prime_number(number):
    if(number < 2):
        return False
    for i in range(2, int_sqrt(number) + 1):
        if number % i == 0:
            return False
    return True


def int_sqrt(number):
    return int(math.sqrt(number))
