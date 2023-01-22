def distinct_power(a, b):
    distinct_powers = set()
    for i in range(2, a + 1):
        for j in range(2, b + 1):
            distinct_powers.add(pow(i, j))

    return len(distinct_powers)


if __name__ == '__main__':
    print(distinct_power(100, 100))
