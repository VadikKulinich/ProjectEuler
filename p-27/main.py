from utils.numbers import is_prime_number


def find_longest_consecutive_primes(a, b):
    count = 0
    a_b_product = 0
    for i in range(-a + 1, a):
        for j in range(-b, b + 1):
            current_count = count_consecutive_primes(i, j)
            if current_count > count:
                a_b_product = i * j
                count = current_count

    return count, a_b_product


def count_consecutive_primes(a, b):
    n = 0
    while True:
        num = n ** 2 + a * n + b
        if not is_prime_number(num):
            return n
        n += 1


if __name__ == '__main__':
    print(find_longest_consecutive_primes(1000, 1000))
