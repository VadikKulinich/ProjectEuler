from utils.numbers import factor_number


def digit_cancelling_faction():
    final_nominator = final_denominator = 1

    def update_final_fraction(n, d):
        nonlocal final_nominator
        nonlocal final_denominator
        if n is not None and d is not None:
            print(n, '/', d)
            final_nominator *= n
            final_denominator *= d

    for nominator in range(10, 100):
        first = nominator // 10
        last = nominator % 10
        for j in range(10):
            n1, d1 = check_fraction(nominator, first * 10 + j, last, j)
            update_final_fraction(n1, d1)

            n2, d2 = check_fraction(nominator, j * 10 + first, last, j)
            update_final_fraction(n2, d2)

            n3, d3 = check_fraction(nominator, last * 10 + j, first, j)
            update_final_fraction(n3, d3)

            n4, d4 = check_fraction(nominator, j * 10 + last, first, j)
            update_final_fraction(n4, d4)

    nominator_factors = factor_number(final_nominator)
    denominator_factors = factor_number(final_denominator)
    for num, count in nominator_factors.items():
        if num in denominator_factors:
            simplified = abs(denominator_factors[num] - count)
            if simplified != 0:
                denominator_factors[num] = simplified
            else:
                del denominator_factors[num]

    simplified_denominator = 1
    for num, count in denominator_factors.items():
        simplified_denominator *= num ** count

    return simplified_denominator


def check_fraction(nominator, denominator, simplified_nominator, simplified_denominator):
    if nominator >= denominator or simplified_nominator >= denominator:
        return None, None
    if denominator == 0 or simplified_denominator == 0:
        return None, None
    if nominator / denominator == simplified_nominator / simplified_denominator:
        if nominator % 10 != 0 and denominator % 10 != 0 and simplified_nominator % 10 != 0 and simplified_denominator % 10 != 0:
            return nominator, denominator
    return None, None


if __name__ == '__main__':
    print(digit_cancelling_faction())
