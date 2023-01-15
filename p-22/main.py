def name_weight(name):
    weight = 0
    for c in name:
        weight += ord(c) - ord('A') + 1

    return weight


def sum_names_score(names):
    names.sort()
    total = 0
    for i in range(len(names)):
        total += (i + 1) * name_weight(names[i])

    return total


if __name__ == '__main__':
    with open("names.txt") as f:
        names = f.readline().split(",")
        print(sum_names_score(names))
