import utils.numbers as utils


def find_n_prime(n):
    i = 0
    number = 2
    while i != n:
        if utils.is_prime_number(number):
            i += 1
        number += 1
    return number - 1


if __name__ == "__main__":
    print(find_n_prime(10001))
