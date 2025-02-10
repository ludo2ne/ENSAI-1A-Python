def incluse(a, b) -> bool:
    """Vérifie si tous les caractères d'une chaîne sont inclus dans une autre.

    Parameters
    ----------
    a : str
        chaîne avec les caractères à rechercher
    b : str
        chaîne à vérifier

    Returns
    -------
    bool
        True si et seulement si b contient tous les caractères de a.
    """
    for c in a:
        if c not in b:
            return False
    return True


def incluse_short(a, b) -> bool:
    # print([x in b for x in a])
    return all(x in b for x in a)


print(incluse("psa", "abcdpsxyz+-012"))
print(incluse_short("psa", "abcdpsxyz+-012"))


def verifier_entier_valide(val, inf=None, sup=None) -> bool:
    """Vérifie qu'une chaîne représente un entier dans un interval.

    Parameters
    ----------
    val : str
        chaîne à vérifier
    inf : int
        borne inférieure (None par défaut)
    sup : int
        borne supérieure (None par défaut)

    Returns
    -------
    bool
        True si val est un entier entre inf et sup
    """
    if not incluse(val, "0123456789"):
        return False

    return (inf is None or int(val) >= inf) and (sup is None or int(val) <= sup)


print(verifier_entier_valide("10"))
print(verifier_entier_valide("10", 50))
print(verifier_entier_valide("10", 0, 20))
