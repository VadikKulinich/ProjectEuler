triangle_digits = {i * (i + 1) // 2 for i in range(1, 27)}


def is_triangle(word):
    char_sum = 0
    for c in word:
        char_sum += ord(c) - 64

    return char_sum in triangle_digits


def find_all_triangle_words(words):
    counter = 0
    for word in words:
        if is_triangle(word):
            counter += 1

    return counter


def find_all_triangle_words_from_file():
    with open("words.txt") as f:
        content = f.read()
        content = content.replace("\"", "")
        return find_all_triangle_words(words=content.split(","))


if __name__ == '__main__':
    print(find_all_triangle_words_from_file())
