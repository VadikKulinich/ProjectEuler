def sum_all_pandigital_numbers():
    complementary_sizes = {0: 4, 1: 2, 3: 0}
    digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    numbers_to_pick = set()
    for size, complementary in complementary_sizes.items():
        start = 10 ** size
        end = 10 ** (size + 1)
        comp_start = 10 ** complementary
        comp_end = 10 ** (complementary + 1)
        for i in range(start, end):
            for j in range(comp_start, comp_end):
                multiplication = i * j
                nums_str = '{}{}{}'.format(i, j, multiplication)
                if len(nums_str) == 9:
                    has_all_digits = True
                    for n in digits:
                        if n not in nums_str:
                            has_all_digits = False
                            break
                    if has_all_digits:
                        numbers_to_pick.add(multiplication)

    return sum(numbers_to_pick)


if __name__ == '__main__':
    print(sum_all_pandigital_numbers())
