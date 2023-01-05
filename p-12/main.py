from utils.numbers import sum_natural, factor_number


def find_number_with_factors(number_factors):
    counter = 1
    while True:
        triangle_number = sum_natural(counter)
        factors = factor_number(triangle_number)
        divisors = divisor_counter(factors)
        if divisors >= number_factors:
            return triangle_number
        else:
            counter += 1


def divisor_counter(factors):
    counter = 1
    for count in factors.values():
        counter *= (count + 1)

    return counter


if __name__ == '__main__':
    print(find_number_with_factors(500))
