def count_right_triangles(p):
    max_a = p // 3
    counter = 0
    for a in range(1, max_a):
        if (p ** 2 - 2 * a * p) % (2 * p - 2 * a) == 0:
            counter += 1

    return counter


def find_max_right_triangles(perimeter_bound):
    max_counter = 0
    max_p = 0
    for i in range(perimeter_bound + 1):
        counter = count_right_triangles(i)
        if counter > max_counter:
            max_counter = counter
            max_p = i

    return max_p


if __name__ == '__main__':
    print(find_max_right_triangles(1000))
