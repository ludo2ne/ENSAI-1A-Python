def count_valid_words(text):
    res = 0
    lines = text.splitlines()

    for line in lines:
        rule, word = line.split(": ")
        parts = rule.split()
        min_occurrences, max_occurrences = map(int, parts[0].split("-"))
        required_char = parts[1][0]

        char_count = word.count(required_char)

        if min_occurrences <= char_count <= max_occurrences:
            res += 1

    return res


def count_sequences(text):
    res = 0
    lines = text.splitlines()

    previous = False
    seq = False

    for line in lines:
        rule, word = line.split(": ")
        parts = rule.split()
        min_occurrences, max_occurrences = map(int, parts[0].split("-"))
        required_char = parts[1][0]

        char_count = word.count(required_char)

        if previous:
            if min_occurrences <= char_count <= max_occurrences:
                seq = True
                res += 1
            else:
                previous = False
                if seq:
                    res += 1
                seq = False
        else:
            if min_occurrences <= char_count <= max_occurrences:
                previous = True

    return res


if __name__ == "__main__":
    from pathlib import Path

    file_path = Path(__file__).resolve().parent.parent / "data/valid.txt"
    text_input = open(file_path, "r").read()

    example1 = """1-2 a: abcdefgh
                  1-3 z: abcdef
                  2-4 x: xxxxxxx"""
    example1 = "\n".join([line.strip() for line in example1.splitlines()])

    print("example1 : ", count_valid_words(example1))
    print("f1 : ", count_valid_words(text_input))

    print("-" * 100)

    example2 = """1-2 a: a
                  1-3 z: zzz
                  1-4 t: tt
                  3-4 x: ggggg
                  1-2 b: b
                  3-4 x: ggggg"""
    example2 = "\n".join([line.strip() for line in example2.splitlines()])

    print("example2 : ", count_sequences(example2))
    print("f2 : ", count_sequences(text_input))
