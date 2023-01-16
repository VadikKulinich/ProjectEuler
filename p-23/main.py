from utils.numbers import sum_proper_divisors


def is_abundant(number):
    return sum_proper_divisors(number) > number


def sum_non_abundant_numbers():
    abundant_numbers = set()
    for i in range(1, 28124):
        if is_abundant(i):
            abundant_numbers.add(i)

    sum_non_abundant = 0
    for i in range(1, 28124):
        non_abundant = True
        for num in abundant_numbers:
            if i - num in abundant_numbers:
                non_abundant = False
                break
        if non_abundant:
            sum_non_abundant += i

    return sum_non_abundant


if __name__ == '__main__':
    print(sum_non_abundant_numbers())

