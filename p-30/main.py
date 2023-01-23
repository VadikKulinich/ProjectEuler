def sum_all_power_numbers(target_power):
    numbers_sum = 0
    for i in range(10, (9 ** target_power) * target_power):
        sum_digit_powers = 0
        current_number = i
        while current_number > 0:
            sum_digit_powers += int(pow(current_number % 10, target_power))
            current_number = current_number // 10
        if sum_digit_powers == i:
            numbers_sum += i

    return numbers_sum


if __name__ == '__main__':
    print(sum_all_power_numbers(4))
