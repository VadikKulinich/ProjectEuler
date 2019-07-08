def generate_fib_numbers(upper_bound, filter):
    first = 0
    second = 1
    current = first
    while current < upper_bound:
        if filter(current):
            yield current
        current = second
        second += first
        first = current


print(sum(generate_fib_numbers(4_000_000, lambda n: n % 2 == 0)))