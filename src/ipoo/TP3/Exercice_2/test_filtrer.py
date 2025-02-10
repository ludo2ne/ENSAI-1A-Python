import pytest
from filtrer import filtrer


@pytest.mark.parametrize(
    "fonction, liste, expected_result",
    [
        (
            lambda n: n % 2 == 1,
            [1, 2, 3, 4, 5, 6],
            [1, 3, 5],
        ),
        (lambda n: n % 2 == 1, [], []),
        (
            lambda n: n % 2 == 1,
            [2, 4, 6, 8],
            [],
        ),
        (
            lambda n: n % 2 == 1,
            [1, 3, 5],
            [1, 3, 5],
        ),
    ],
)
def test_filtrer(fonction, liste, expected_result):
    # WHEN
    resultat = filtrer(fonction, liste)

    # THEN
    assert resultat == expected_result
