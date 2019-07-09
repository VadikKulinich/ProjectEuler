import utils.numbers as numbers


def find_largest_prime_factor(number):
    for i in range(numbers.int_sqrt(number // 2), 2, -1):
        if number % i == 0 and numbers.is_prime_number(i):
            return i
    return -1


print(find_largest_prime_factor(600851475143))
