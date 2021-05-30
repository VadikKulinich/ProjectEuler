import utils.numbers as utils


def largest_palindrome_product(n):
    largest = 0
    for i in range(n - 1, 0, -1):
        for j in range(i, 0, -1):
            number_to_check = i * j
            if number_to_check < largest:
                break
            if number_to_check == utils.reverse_number(number_to_check) and largest < number_to_check:
                largest = number_to_check
    return largest


if __name__ == "__main__":
    print(largest_palindrome_product(100))
    print(largest_palindrome_product(1000))
