import pytest


def ellipsoide(point, axes) -> bool:
    """vérifier qu'un point appartient à un ellipsoide"""
    if not isinstance(point, tuple):
        raise TypeError(f"{point} doit être une instance de tuple.")

    x, y, z = point
    a, b, c = axes

    return (x / a) ** 2 + (y / b) ** 2 + (z / c) ** 2 == pytest.approx(1)


ellipsoide((1, 2), 4)
