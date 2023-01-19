def find_cycle_number(n):
    base = 1
    numbers = set()
    while base < n:
        base *= 10
    while base != 0:
        new_base = base % n * 10
        if new_base in numbers:
            return new_base
        numbers.add(new_base)
        base = new_base

    return 0


def get_cycle_size(num, n):
    base = num
    counter = 0
    while True:
        new_base = base % n * 10
        counter += 1
        if new_base == num:
            break
        base = new_base

    return counter


def reciprocal_cycles(n):
    cycle_number = 0
    max_cycle = 0
    for i in range(1, n + 1):
        cycle = find_cycle_number(i)
        if cycle != 0:
            size = get_cycle_size(cycle, i)
            if max_cycle < size:
                cycle_number = i
                max_cycle = size

    return cycle_number


if __name__ == '__main__':
    print(reciprocal_cycles(1000))
