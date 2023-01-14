def amicable_pair(n):
    factors_sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            factors_sum += i

    return factors_sum


def sum_amicable_numbers(start, end):
    sum_amicable = 0
    for i in range(start, end + 1):
        i_pair = amicable_pair(i)
        if i == amicable_pair(i_pair) and i != i_pair:
            sum_amicable += i

    return sum_amicable


if __name__ == '__main__':
    print(sum_amicable_numbers(1, 10000))