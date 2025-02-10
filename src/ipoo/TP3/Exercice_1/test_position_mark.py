import pytest
from position import position


@pytest.mark.parametrize(
    "elt, liste, depart, expected_result",
    [
        (3, [1, 2, 3, 4, 5], 0, 2),  # test_position_element_trouve
        (6, [1, 2, 3, 4, 5], 0, -1),  # test_position_element_non_trouve
        (2, [1, 2, 3, 4, 5], 3, -1),  # test_position_apres_depart
        ("a", "ahsdfjhkjdf", 0, 0),
        (2, [1, 2, 3, 4, 5], 10, -1),
    ],
)
def test_position(elt, liste, depart, expected_result):
    # WHEN
    resultat = position(elt, liste, depart)

    # THEN
    assert resultat == expected_result
