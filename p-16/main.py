def sum_digits_of_pow(base, exponent):
    number = int(pow(base, exponent))
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number = number // 10

    return digit_sum


if __name__ == '__main__':
    print(sum_digits_of_pow(2, 1000))
