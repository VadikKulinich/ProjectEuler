from utils.numbers import is_prime_number, factor_number

def is_circular_prime(number):
    if number < 10:
        return is_prime_number(number)
    if number % 1000 % 8 == 0:
        return False
    if number % 100 % 4 == 0:
        return False

    all_digits = []
    current_number = number

    while current_number > 0:
        digit = current_number % 10
        if digit % 2 == 0 or digit == 0:
            return False
        all_digits.append(digit)
        current_number = current_number // 10

    digits_sum = sum(all_digits)
    if digits_sum % 3 == 0:
        return False

    offset = 10 ** (len(all_digits) - 1)
    for i in range(len(all_digits)):
        if not is_prime_number(number):
            return False
        else:
            last_digit = number % 10
            number = number // 10
            number += offset * last_digit

    return True


def count_all_circular_primes(upper_bound):
    numbers = set()
    for i in range(2, upper_bound + 1):
        if is_circular_prime(i):
            numbers.add(i)

    return len(numbers)


if __name__ == '__main__':
    print(count_all_circular_primes(1_000_000))
