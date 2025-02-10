def moyenne_mobile(liste, n) -> list:
    """Calcule la série des moyennes mobile

    Parameters
    ----------
    entree : list
        série de valeurs
    n : int
        période

    Returns
    -------
    list
        Liste des moyennes mobiles
    """
    if n > len(liste):
        raise Exception("nombre de périodes trop grand")

    res = []

    for i, v in enumerate(liste):
        if i + n <= len(liste):
            res.append(sum(liste[i : i + n]) / n)
        else:
            break

    return res


print(moyenne_mobile([2, 3, 5, 7, 11, 13, 17], 4))
