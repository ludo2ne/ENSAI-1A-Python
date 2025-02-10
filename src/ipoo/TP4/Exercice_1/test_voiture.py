import pytest

from voiture import Voiture


@pytest.fixture
def voiture_arretee():
    return Voiture("titine", "bleue")


@pytest.fixture
def voiture_5():
    return Voiture("titine", "bleue", 5)


@pytest.fixture
def voiture_125():
    return Voiture("titine", "bleue", 125)


def test_accelere_ok(voiture_arretee):
    # GIVEN
    v = 5

    # WHEN
    voiture_arretee.accelere(v)

    # THEN
    assert voiture_arretee.vitesse == 5


def test_accelere_max(voiture_arretee):
    # GIVEN
    v = 15

    # WHEN
    voiture_arretee.accelere(v)

    # THEN
    assert voiture_arretee.vitesse == 10


def test_accelere_130(voiture_125):
    # GIVEN
    v = 10

    # WHEN
    voiture_125.accelere(v)

    # THEN
    assert voiture_125.vitesse == 130


def test_accelere_negatif(voiture_125):
    # GIVEN
    v = -10

    # WHEN
    voiture_125.accelere(v)

    # THEN
    assert voiture_125.vitesse == 125


def test_freine_negatif(voiture_5):
    # GIVEN
    v = -10

    # WHEN
    voiture_5.freine(v)

    # THEN
    assert voiture_5.vitesse == 5


def test_freine_zero(voiture_5):
    # GIVEN
    v = 10

    # WHEN
    voiture_5.freine(v)

    # THEN
    assert voiture_5.vitesse == 0


def test_freine(voiture_125):
    # GIVEN
    v = 25

    # WHEN
    voiture_125.freine(v)

    # THEN
    assert voiture_125.vitesse == 100


def test_est_arretee_true(voiture_arretee):
    # GIVEN

    # WHEN
    res = voiture_arretee.est_arretee()

    # THEN
    assert res


def test_est_arretee_false(voiture_125):
    # GIVEN

    # WHEN
    res = voiture_125.est_arretee()

    # THEN
    assert not res
