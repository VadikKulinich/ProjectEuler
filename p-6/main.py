def sum_square_difference(n):
    result = 0
    for i in range(n):
        for j in range(i + 1, n, 1):
            result += 2 * (i + 1) * (j + 1)
    return result


if __name__ == "__main__":
    print(sum_square_difference(100))
