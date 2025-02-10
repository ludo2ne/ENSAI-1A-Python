def afficher_titre(texte, largeur, alignement="centrer") -> None:
    """Affiche le texte centré dans la largeur indiquée et bordé d'astérisques.

    Parameters
    ----------
    texte : list
        le texte à mettre en forme sous forme de liste
    largeur : int
        largeur demandée
        si la valeur largeur est trop petite, alors la fonction utilise une largeur
        adaptée à la plus longue ligne du texte.
    alignement: str
        centrer, gauche ou droite

    Returns
    -------
    None

    Examples
    --------
    >>> afficher_titre(['a'], 1)
    ***
    *a*
    ***
    """

    match alignement:
        case "centrer":
            aligner = "^"
        case "droite":
            aligner = ">"
        case "gauche":
            aligner = "<"
        case _:
            return "Argument alignement non valide"

    taille_max = max(len(ligne) for ligne in texte)
    taille_max = max(taille_max, largeur)

    print("*" * (taille_max + 2))

    for ligne in texte:
        print("*{:{}{}}*".format(ligne, aligner, taille_max))

    print("*" * (taille_max + 2))


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

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    afficher_titre(texte, 50)
    afficher_titre(texte, 50, "droite")
