from position import position


def sous_liste(petite_liste, grande_liste):
    """Les éléments de petite_liste sont-ils tous, et dans
    le même ordre, dans grande_liste?

    Parameters
    ------------
    petite_liste: list

    grande liste: list

    Returns
    -----------
    Bool: True si petite_liste est une sous-liste de grande_liste
          False sinon

    """
    if not isinstance(petite_liste, list):
        raise TypeError("petite_liste doit être une liste")
    if not isinstance(grande_liste, list):
        raise TypeError("grande_liste doit être une liste")
    if len(petite_liste) > len(grande_liste):
        raise TypeError("petite_liste doit être plus grande que grande_liste")
    indice_elem_precedent = 0
    for element in petite_liste:
        if (
            position(element, grande_liste, indice_elem_precedent)
            <= indice_elem_precedent
        ):
            return False
        else:
            indice_elem_precedent = position(element, grande_liste, 0) + 1
    return True
