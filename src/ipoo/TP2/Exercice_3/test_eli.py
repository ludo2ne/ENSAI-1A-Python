import re

import pytest
from ellipsoide import ellipsoide


@pytest.mark.parametrize(
    "point, axes, erreur, message_erreur",
    [
        (
            [1, 2, 3], (4, 5, 6), TypeError, "[1, 2, 3] doit être une instance de tuple.",
        ),
    ],
)
def test_ellipsoide_parametres(point, axes, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        ellipsoide(point, axes)


@pytest.mark.parametrize(
    "point, axes, resultat_attendu",
    [
        ((1, 0, 0), (1, 1, 1), True),
        ((0, 0, 0), (1, 1, 1), False),
    ],
)
def test_ellipsoide_resultats(point, axes, resultat_attendu):
    assert ellipsoide(point, axes) == resultat_attendu
