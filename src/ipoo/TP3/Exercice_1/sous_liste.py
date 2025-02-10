from position import position


def sous_liste(petite_liste, grande_liste) -> bool:
    """
    Vérifie si tous les éléments de petite_liste apparaissent dans grande_liste dans
    le même ordre.

    Parameters
    ----------
    petite_liste : list
        La liste d'éléments à rechercher dans `grande_liste`.
    grande_liste : list
        La liste dans laquelle rechercher les éléments de `petite_liste`.

    Returns
    -------
    bool
        Retourne True si tous les éléments de petite_liste apparaissent dans
        grande_liste dans le même ordre, autrement `False` si un élément est manquant
        ou mal ordonné.

    Examples
    --------
    >>> sous_liste([2, 4], [1, 2, 3, 4, 5])
    True
    >>> sous_liste([5, 2], [1, 2, 3, 4, 5])
    False
    """
    if len(petite_liste) > len(grande_liste):
        raise TypeError("Petite liste doit être plus petite que grande liste")
    pos = 0
    for el in petite_liste:
        pos = position(elt=el, liste=grande_liste, depart=pos)
        if pos == -1:
            return False
        pos += 1
    return True
