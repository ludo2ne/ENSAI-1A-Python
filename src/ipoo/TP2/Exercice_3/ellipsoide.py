import pytest


def verif_tuple_digit_three(t, positif=False) -> bool:
    """Vérfie si le paramètre t est un tuple de 3 éléments contenant des nombres."""

    if not isinstance(t, tuple):
        raise TypeError(f"{t} doit être une instance de tuple.")

    if not len(t) == 3:
        raise ValueError(f"{t} doit être de longueur 3.")

    for element in t:
        if not (isinstance(element, int) or isinstance(element, float)):
            raise ValueError(
                f"Tous les éléments de {t} doivent être des instances de int ou float."
            )
        if positif and not element > 0:
            raise ValueError(
                f"Tous les éléments de {t} doivent être strictement positifs."
            )

    return True


def ellipsoide(point, axes):
    """Détermine si un point fait partie de l'ellipsoïde.

    L'équation de l'ellipsoïde est :
        (x / a) ** 2 + (y / b) ** 2 (z / c) ** 2 == 1
    pour un point de coordonnées cartésiennes (x, y, z) et
    où a, b, c sont les demi-axes de l'ellipsoïde.

    Parameters
    ----------
    point : tuple[int or float]
        Coordonnées cartésiennes du point.
    axes : tuple[int or float]
        Demi-axes de l'ellipsoïde.

    Returns
    -------
    bool
        True si le point fait partie de l'ellipsoïde, False sinon.

    Examples
    --------
    >>> ellipsoide((1, 0, 0), (1, 1, 1))
    True
    >>> ellipsoide((2, 0, 0), (1, 1, 1))
    False
    >>> ellipsoide((2, 3, 4), (2, 3, 4))
    False
    """

    verif_tuple_digit_three(point)
    verif_tuple_digit_three(axes, True)

    x, y, z = point
    a, b, c = axes

    return (x / a) ** 2 + (y / b) ** 2 + (z / c) ** 2 == pytest.approx(1)
