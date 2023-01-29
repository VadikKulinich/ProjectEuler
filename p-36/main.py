def is_double_palindrome(n):
    reversed_n = 0
    current = n
    while current > 0:
        reversed_n = reversed_n * 10 + current % 10
        current = current // 10

    if n != reversed_n:
        return False

    binary = str(bin(n))[2:]  # remove 0b
    return binary == binary[::-1]


def sum_all_double_palindromes(upper_bound):
    double_palindromes_sum = 0
    for i in range(1, upper_bound + 1):
        if is_double_palindrome(i):
            print(i)
            double_palindromes_sum += i

    return double_palindromes_sum


if __name__ == '__main__':
    print(sum_all_double_palindromes(1_000_000))
