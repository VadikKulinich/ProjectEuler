from utils.numbers import fibonacci


def index_of_fib_number(size):
    n = 1
    while True:
        number = fibonacci(n)
        if len(str(number)) == size:
            return n
        n += 1


if __name__ == '__main__':
    print(index_of_fib_number(size=1000))
