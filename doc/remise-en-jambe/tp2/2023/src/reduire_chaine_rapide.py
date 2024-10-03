def reduction_rapide(texte) -> int:
    if not texte.isalpha():
        print("La chaîne doit contenir uniquement des caractères alphabétiques.")
        return None

    # Liste pour stocker les caractères qui n'ont pas encore réagit
    sortie = []

    # On parcourt les caractères du texte 1 à 1
    for c in texte:
        # Si sortie est non vide et si le caractère courant réagit avec le dernier caractère de la sortie
        if (
            sortie and c == sortie[-1].swapcase()
        ):  # la fonction swapcase transforme une majuscule en minuscule et inversement
            sortie.pop()  # Alors on supprime le dernier caractère de la sortie
        else:
            sortie.append(c)  # Sinon on l'ajoute à la sortie

    return len(sortie)


if __name__ == "__main__":
    # Import du fichier

    from pathlib import Path

    file_path = Path(__file__).resolve().parent.parent / "data/reduction.txt"
    text_input = open(file_path, "r").read()

    print(reduction_rapide(text_input))
    print(
        min(
            reduction_rapide(text_input.replace(c, "").replace(c.upper(), ""))
            for c in set(text_input.lower())
        )
    )

    print("-" * 100)

    # En détaillant un peu plus
    #   pour chacun des caractères présents dans texte
    #   on calcule la réduction rapide en supprimant toutes les occurences de ce caractère (majuscule et minuscule)
    for c in sorted(set(text_input.lower())):
        print(
            c,
            ":",
            reduction_rapide(text_input.replace(c, "").replace(c.upper(), "")),
            end=" - ",
            sep="",
        )
