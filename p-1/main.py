def check_is_divisible(dividers, number):
    if number == 1 or dividers is []:
        return False
    for n in dividers:
        if number % n == 0:
            return True
    return False


def filter_numbers(dividers, upper_bound, lower_bound=1):
    current = lower_bound
    while current < upper_bound:
        if(check_is_divisible(dividers, current)):
            yield current
        current += 1


print(sum(filter_numbers([3, 5], 1000)))
