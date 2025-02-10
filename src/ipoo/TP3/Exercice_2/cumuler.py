from functools import reduce


def cumuler(fonction, liste):
    """Applique une fonction binaire pour cumuler les éléments de la liste.

    Parameters
    ----------
    fonction : function
        Une fonction prenant deux arguments et retournant un résultat.
    liste : list
        La liste des éléments à cumuler.

    Returns
    -------
    any
        Le résultat de l'application cumulative de la fonction binaire.

    Raises
    ------
    ValueError
        Si la liste contient moins de deux éléments.
    """
    if len(liste) < 2:
        raise ValueError("La liste doit contenir au moins deux éléments.")

    resultat = liste[0]
    for i in range(1, len(liste)):
        resultat = fonction(resultat, liste[i])
    return resultat


def cumuler_reduce(fonction, liste):
    if len(liste) < 2:
        raise ValueError("La liste doit contenir au moins deux éléments.")

    return reduce(fonction, liste)
