from utils.numbers import is_prime_number


def is_truncatable_prime(n):
    power = 1
    current = n // (10 ** power)
    while current > 0:
        current = n // (10 ** power)
        reversed_n = n % (10 ** power)
        if not is_prime_number(reversed_n) or current > 0 and not is_prime_number(current):
            return False
        power += 1

    return True


def sum_all_truncatable_numbers(count):
    sum_number = 0
    counter = 0
    current = 10
    while counter < count:
        if is_truncatable_prime(current):
            sum_number += current
            counter += 1
        current += 1

    return sum_number


if __name__ == '__main__':
    print(sum_all_truncatable_numbers(11))
