from math import sqrt, gcd


def find_special_pythagorean_triplet(target_sum):
    s = target_sum / 2
    m_limit = int(sqrt(s)) - 1
    for m in range(2, m_limit + 1):
        if s % m == 0:
            sm = s // m
            while sm % 2 == 0:
                sm = sm // 2
            if m % 2 == 1:
                k = m + 2
            else:
                k = m + 1
            while k < 2 * m and k <= sm:
                if sm % k == 0 and gcd(k, m) == 1:
                    d = int(s // (k * m))
                    n = k - m
                    a = d * (m * m - n * n)
                    b = 2 * d * m * n
                    c = d * (m * m + n * n)
                    return a * b * c
                k = k + 2
    return -1


if __name__ == '__main__':
    print(find_special_pythagorean_triplet(1000))
