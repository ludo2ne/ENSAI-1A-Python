import pytest
from sous_liste import sous_liste


@pytest.mark.parametrize(
    "petite_liste, grande_liste, expected_result",
    [
        (
            [2, 4],
            [1, 2, 3, 4, 5],
            True,
        ),  # Cas OK : tous les éléments sont dans le même ordre
        (
            [2, 6],
            [1, 2, 3, 4, 5],
            False,
        ),  # Cas où certains éléments ne sont pas dans grande_liste
        (
            [3, 1, 5],
            [1, 2, 3, 4, 5],
            False,
        ),  # Cas où les éléments sont dans la grande liste mais pas dans le même ordre
        (
            [3, 1, 5],
            [1, 2, 3, 1],
            False,
        ),
    ],
)
def test_sous_liste(petite_liste, grande_liste, expected_result):
    # WHEN
    resultat = sous_liste(petite_liste, grande_liste)

    # THEN
    assert resultat == expected_result


@pytest.mark.parametrize(
    "petite_liste, grande_liste, type_exception, message",
    [
        (
            [1, 2, 3],
            [0, 1],
            TypeError,
            "Petite liste doit être plus petite que grande liste",
        ),
    ],
)
def test_est_impair_valeurs_invalides(
    petite_liste, grande_liste, type_exception, message
):
    # WHEN / THEN
    with pytest.raises(type_exception, match=message):
        sous_liste(petite_liste, grande_liste)
