def afficher_titre(texte, largeur, align="centre") -> None:
    """Affiche joliement un texte

    Parameters
    ----------
    texte : list
        Une liste de chaînes de caractères, chaque élément étant une ligne
    largeur : int
        La largeur minimale du cadre à afficher
    align : {'centre', 'gauche', 'droite'}
        Alignement du texte (valeur par défaut : centre)

    """

    if align == "gauche":
        align_code = "<"
    elif align == "droite":
        align_code = ">"
    else:
        align_code = "^"

    largeur_max = max(largeur, max([len(txt) for txt in texte]))
    print(largeur_max)

    res = "*" * (largeur_max + 2) + "\n"

    for txt in texte:
        res += "*{:{}{}}*\n".format(txt, align_code, largeur_max)

    res += "*" * (largeur_max + 2)

    print(res)


texte = [
    "L'ingénieux hidalgo",
    "Don Quichotte de la Manche",
    "",
    "Composé par Miguel de Cervantes",
    "",
    "Avec privilège royal",
    "à Madrid",
    "en l'an de grâce 1605",
]

afficher_titre(texte, 33)
