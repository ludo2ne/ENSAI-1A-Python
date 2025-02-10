def position(elt, liste, depart) -> int:
    """
    Recherche la position d'un élément dans une liste à partir d'un indice donné.

    Parameters
    ----------
    elt :
        L'élément à rechercher dans la liste.
    liste : list
        La liste dans laquelle effectuer la recherche.
    depart : int
        L'indice à partir duquel commencer la recherche.

    Returns
    -------
    int
        L'indice de la première occurrence de `elt` dans `liste` après `depart`.
        Retourne -1 si l'élément n'est pas trouvé.

    Examples
    --------
    >>> position(3, [1, 2, 3, 4, 3], 2)
    2
    >>> position(5, [1, 2, 3, 4], 0)
    -1
    """
    for i in range(depart, len(liste)):
        if liste[i] == elt:
            return i
    return -1
