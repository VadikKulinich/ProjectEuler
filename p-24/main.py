from math import factorial


def lexicographical_order(num_set, item_to_pick):
    n = len(num_set)
    num_set.sort()
    max_items = factorial(n)
    if item_to_pick > max_items:
        return -1

    current_bucket = 0
    result_str = ''
    while len(num_set) > 0:
        bucket_size = max_items // len(num_set)
        bucket_upper_bound = (current_bucket + 1) * bucket_size
        if item_to_pick <= bucket_upper_bound:
            max_items = max_items // len(num_set)
            result_str = result_str + str(num_set[current_bucket])
            del num_set[current_bucket]
            item_to_pick -= current_bucket * bucket_size
            current_bucket = 0
        else:
            current_bucket += 1

    return result_str


if __name__ == '__main__':
    print(lexicographical_order([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 1_000_000))
