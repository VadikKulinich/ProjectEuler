def lattice_path(row, col):
    k = row
    n = row + col
    nominator = 1
    denominator = 1
    for i in range(n - k):
        nominator *= (n - i)
    for i in range(k):
        denominator *= (k - i)

    return nominator // denominator


if __name__ == '__main__':
    print(lattice_path(20, 20))
