def diagonal_sum_of_spiral_matrix(n):
    diagonal_sum = 1
    for i in range(3, n + 1, 2):
        for j in range(4):
            diagonal_sum += i ** 2 - j * (i - 1)
    return diagonal_sum


if __name__ == '__main__':
    print(diagonal_sum_of_spiral_matrix(1001))
