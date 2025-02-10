def filtrer(fonction, liste):
    """Filtre les éléments de la liste en gardant ceux pour lesquels fonction(element) est True.

    Parameters
    ----------
    fonction : function
        Une fonction qui prend un élément et retourne un booléen.
    liste : list
        La liste des éléments à filtrer.

    Returns
    -------
    list
        Une nouvelle liste contenant uniquement les éléments validés par fonction.
    """
    res = []
    for el in liste:
        if fonction(el) is True:
            res.append(el)
    return res


def filtrer_comprehension(fonction, liste):
    return [el for el in liste if fonction(el)]
