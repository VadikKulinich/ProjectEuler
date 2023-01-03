from utils.numbers import is_prime_number


def sum_primes(upper_bound):
    primes_sum = 0
    for i in range(2, upper_bound + 1):
        if is_prime_number(i):
            primes_sum += i

    return primes_sum


if __name__ == '__main__':
    print(sum_primes(2_000_000))