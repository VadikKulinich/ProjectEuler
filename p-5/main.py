import utils.numbers as utils


def smallest_multiple(n):
    all_factors = dict()
    for i in range(n):
        current_factors = utils.factor_number(i + 1)
        for number, frequency in current_factors.items():
            all_factors[number] = max(frequency, all_factors.get(number, 0))
    result = 1
    for number, frequency in all_factors.items():
        result *= pow(number, frequency)
    return result


if __name__ == "__main__":
    print(smallest_multiple(20))
