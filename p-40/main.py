from math import log10


def get_digit_of_natural_sequence(index):
    current_index = 1
    current_digit = 1
    step = 1
    while current_index < index:
        current_digit += 1
        power = log10(current_digit)
        if power == int(power):
            step += 1
        current_index += step
    while current_index > index:
        current_digit = current_digit // 10
        current_index -= 1

    return current_digit % 10


def find_product_of_digits():
    product = 1
    for i in range(7):
        index = 10 ** i
        product *= get_digit_of_natural_sequence(index)

    return product


if __name__ == '__main__':
    print(find_product_of_digits())
