import re

import pytest
from ellipsoide import ellipsoide


@pytest.mark.parametrize(
    'params, erreur, message_erreur',
    [
        ({'point': [1, 2, 3], 'axes': (4, 5, 6)}, TypeError,
         "[1, 2, 3] doit être une instance de tuple."),
        ({'point': (1, 2, 3), 'axes': [4, 5, 8]}, TypeError,
         "[4, 5, 8] doit être une instance de tuple."),
        ({'point': (0, 1), 'axes': (2, 3, 4)}, ValueError,
         "(0, 1) doit être de longueur 3."),
        ({'point': (0, 1, 2), 'axes': (3, 4, 4, 5)}, ValueError,
         "(3, 4, 4, 5) doit être de longueur 3."),
        ({'point': (0, [1], 2), 'axes': (3, 4, 5)}, ValueError,
         "Tous les éléments de (0, [1], 2) doivent être des instances de int ou float."),
        ({'point': (0, 1, 2), 'axes': (3, '4', 5)}, ValueError,
         "Tous les éléments de (3, '4', 5) doivent être des instances de int ou float."),
        ({'point': (0, 1, 2), 'axes': (1, 0, 1)}, ValueError,
         "Tous les éléments de (1, 0, 1) doivent être strictement positifs."),
        ({'point': (0, 1, 2), 'axes': (1, 2, -1)}, ValueError,
         "Tous les éléments de (1, 2, -1) doivent être strictement positifs.")
    ]
)
def test_ellipsoide_parametres(params, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        ellipsoide(**params)


@pytest.mark.parametrize(
    'params, resultat_attendu',
    [
        ({'point': (1, 0, 0), 'axes': (1, 1, 1)}, True),
        ({'point': (0, 1, 0), 'axes': (1, 1, 1)}, True),
        ({'point': (0, 0, 1), 'axes': (1, 1, 1)}, True),
        ({'point': (0, 0, 0), 'axes': (1, 1, 1)}, False),
        ({'point': (1, 1, 1), 'axes': (1, 1, 1)}, False),
        ({'point': (2, 0, 0), 'axes': (2, 3, 4)}, True),
        ({'point': (0, 3, 0), 'axes': (2, 3, 4)}, True),
        ({'point': (0, 0, 4), 'axes': (2, 3, 4)}, True),
        ({'point': (1, (4.5) ** 0.5, 2), 'axes': (2, 3, 4)}, True),
        ({'point': (-1, -(4.5) ** 0.5, -2), 'axes': (2, 3, 4)}, True),
        ({'point': (-1, (4.5) ** 0.5, -2), 'axes': (2, 3, 4)}, True),
        ({'point': (1, (4.5) ** 0.5, -2), 'axes': (2, 3, 4)}, True),
        ({'point': (1, (5.5) ** 0.5, -2), 'axes': (2, 3, 4)}, False),
    ]
)
def test_ellipsoide_resultats(params, resultat_attendu):
    assert ellipsoide(**params) == resultat_attendu
