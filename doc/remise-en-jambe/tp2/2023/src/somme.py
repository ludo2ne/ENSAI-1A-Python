from string import ascii_letters


def part1(text):
    lines = text.splitlines()

    res = 0
    for line in lines:
        middle = len(line) // 2
        str_left, str_right = line[:middle], line[middle:]

        common_letter = list(set(str_left) & set(str_right))[0]
        p = ascii_letters.index(common_letter) + 1
        res += p

    return res


def part2(text):
    lines = text.splitlines()

    res = 0
    for line in lines:
        middle = len(line) // 2
        str_left, str_right = line[:middle], line[middle:]

        common_letter = list(set(str_left) & set(str_right))[0]

        if common_letter.isupper() and "A" in line.upper():
            p = ascii_letters.index(common_letter) + 1
            res += p

    return res


if __name__ == "__main__":
    text_input = open("annales/2023-2024/data/items.txt", "r").read()

    example = """ABcCaB
                 xyZpZq
                 abcdefABeCDA"""

    example = "\n".join([line.strip() for line in example.splitlines()])

    print("Exemple - partie 1 : ", part1(example))
    print("Exemple - partie 2 : ", part2(example))

    print("Partie 1 : ", part1(text_input))
    print("Partie 2 : ", part2(text_input))
