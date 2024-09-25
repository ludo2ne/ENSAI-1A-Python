"""
Remise en jambe - TP Noté
12/09/2024
Élève 1 : ?
Élève 2 : ?
"""


def ma_fonction(texte) -> int:
    lines = texte.splitlines()
    res = 0

    for line in lines:
        elements_str = line.split()

        # Convert elements to int
        elements_int = []
        for el in elements_str:
            elements_int.append(int(el))

        res += max(elements_int) - min(elements_int)

    return res


if __name__ == "__main__":

    from pathlib import Path

    file_path = Path(__file__).resolve().parent.parent / "data/somme.txt"
    text_input = open(file_path, "r").read()

    exemple = """4 1 9 5
7 5 3
2 4 4 8"""
    print(ma_fonction(exemple), ma_fonction(exemple) == 18)

    resultat = ma_fonction(text_input)
    print(resultat)  # obtained result : 36174
