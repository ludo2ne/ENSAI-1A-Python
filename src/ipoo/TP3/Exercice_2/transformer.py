def transformer(fonction, liste):
    """Applique une fonction à chaque élément d'une liste.

    Parameters
    ----------
    fonction : function
        la fonction à appliquer
    liste : list
        la liste à transformer

    Returns
    -------
    list
        la liste transformée
    """
    res = []
    for el in liste:
        res.append(fonction(el))
    return res


def transformer_comprehension_liste(fonction, liste):
    return [fonction(el) for el in liste]


def transformer_map(fonction, liste):
    return list(map(fonction, liste))
