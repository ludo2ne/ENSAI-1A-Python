import pytest
from cumuler import cumuler


@pytest.mark.parametrize(
    "fonction, liste, expected_result",
    [
        (lambda x, y: x + y, [0, 1, 2, 3, 4, 5], 15),
        (lambda x, y: x * y, [1, 2, 3, 4], 24),
    ],
)
def test_cumuler(fonction, liste, expected_result):
    # WHEN
    resultat = cumuler(fonction, liste)

    # THEN
    assert resultat == expected_result


def test_cumuler_erreur_si_moins_de_deux_elements():
    # GIVEN
    liste = [8]

    # WHEN / THEN
    with pytest.raises(
        ValueError, match="La liste doit contenir au moins deux éléments."
    ):
        cumuler(lambda x, y: x + y, liste)
