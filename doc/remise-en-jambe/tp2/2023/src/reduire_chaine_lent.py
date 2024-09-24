def reaction(a, b):
    """Teste si 2 caractères vont réagir entre eux"""

    return (a != b) & (a.lower() == b.lower())


def reduction(texte):
    """Réduction simple d'une chaine de caractères"""

    for i in range(len(texte) - 1):
        if reaction(texte[i], texte[i + 1]):
            return texte[:i] + texte[i + 2 :]
    return texte


def reduction_multiple(texte):
    """Réduction d'une chaine de caractères tant que celle-ci n'est pas stable"""

    if not texte.isalpha():
        print("Chaine en paramètre non alphabétique")
        return None

    texte_avant = texte
    while True:
        texte_apres = reduction(texte_avant)
        if texte_apres == texte_avant:
            return texte_apres
        else:
            texte_avant = texte_apres


if __name__ == "__main__":
    # Tests avec les exemples données
    print("Tests.....")
    print("ze" == reduction_multiple("zrRYye"))
    print("abCdABcA" == reduction_multiple("abCdABcA"))
    print("abAb" == reduction_multiple("abCdeEDcAb"))

    print("-" * 100)

    # Import du fichier
    text = open("annales/2023-2024/data/reduction.txt", "r").read()

    rd = reduction_multiple(text)
    print(len(rd))
