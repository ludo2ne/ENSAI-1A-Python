import pytest
from transformer import transformer


@pytest.mark.parametrize(
    "fonction, liste, expected_result",
    [
        (lambda x: x**2, [1, 2, 3, 4], [1, 4, 9, 16]),
        (lambda x: x**2, [], []),
        (lambda x: x**2, [-2, -1, 0], [4, 1, 0]),
    ],
)
def test_transformer(fonction, liste, expected_result):
    # WHEN
    resultat = transformer(fonction, liste)

    # THEN
    assert resultat == expected_result
