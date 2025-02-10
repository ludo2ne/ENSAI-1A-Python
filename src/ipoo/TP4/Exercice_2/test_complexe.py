from complexe import Complexe


def test_addition():
    # GIVEN
    z1 = Complexe(3, 4)
    z2 = Complexe(1, 2)

    # WHEN
    result = z1 + z2

    # THEN
    assert result.reel == 4
    assert result.imaginaire == 6


def test_soustraction():
    # GIVEN
    z1 = Complexe(5, 7)
    z2 = Complexe(2, 3)

    # WHEN
    result = z1 - z2

    # THEN
    assert result.reel == 3
    assert result.imaginaire == 4


def test_multiplication():
    # GIVEN
    z1 = Complexe(2, 3)
    z2 = Complexe(4, -5)

    # WHEN
    result = z1 * z2

    # THEN
    assert result.reel == 23
    assert result.imaginaire == 2
