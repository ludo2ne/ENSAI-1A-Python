from position import position


def test_position_element_trouve():
    # GIVEN
    elt = 3
    liste = [1, 2, 3, 4, 5]
    depart = 0

    # WHEN
    resultat = position(elt, liste, depart)

    # THEN
    assert resultat == 2


def test_position_element_non_trouve():
    # GIVEN
    elt = 6
    liste = [1, 2, 3, 4, 5]
    depart = 0

    # WHEN
    resultat = position(elt, liste, depart)

    # THEN
    assert resultat == -1


def test_position_apres_depart():
    # GIVEN
    elt = 2
    liste = [1, 2, 3, 4, 5]
    depart = 3

    # WHEN
    resultat = position(elt, liste, depart)

    # THEN
    assert resultat == -1
