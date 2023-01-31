from utils.numbers import digits_of

digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def is_pandigital(n):
    n_digits = digits_of(n)

    return len(n_digits) == 9 and set(n_digits) == digits


def concatenated_product(a: int, n: int) -> int:
    vals = [i * a for i in range(1, n + 1)]
    z = 0
    for val in vals:
        z = z * (10 ** len(digits_of(val))) + val

    return z


def find_max_pandigital_product():
    answer = 918273645

    bounds = {2: (1234, 10 ** 4), 3: (123, 10 ** 3), 4: (12, 10 ** 2), 5: (1, 10 ** 1), 6: (1, 10 ** 1),
              7: (1, 10 ** 1), 8: (1, 10 ** 1), 9: (1, 10 ** 1)}

    for n in range(2, 10):
        for a in range(*bounds[n]):
            concat_prod = concatenated_product(a, n)
            if is_pandigital(concat_prod):
                answer = max(answer, concat_prod)

    return answer


if __name__ == '__main__':
    print(find_max_pandigital_product())
