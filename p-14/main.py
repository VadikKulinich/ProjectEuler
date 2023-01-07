def collatz_sequence_size(current):
    counter = 0
    while current != 1:
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1
        counter += 1

    return counter


def find_largest_collatz_sequence(limit):
    max_size = 0
    max_n = 0
    for i in range(limit):
        current_size = collatz_sequence_size(i + 1)
        if current_size > max_size:
            max_n = i + 1
            max_size = current_size
    return max_size, max_n


if __name__ == '__main__':
    print(find_largest_collatz_sequence(1_000_000))
