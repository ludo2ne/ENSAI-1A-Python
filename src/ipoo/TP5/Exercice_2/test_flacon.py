from flacon import Flacon


def test_str():
    # GIVEN
    flacon = Flacon("Sirop de Fraise", 500)

    # WHEN
    result = str(flacon)

    # THEN
    assert result == "Flacon Sirop de Fraise, 500mL, rempli de 0mL concentré à 0%."


def test_remplir_succes():
    # GIVEN
    flacon = Flacon("Sirop de Menthe", 500)

    # WHEN
    success = flacon.remplir(100, 200)

    # THEN
    assert success is True
    assert flacon.volume == 300
    assert flacon.concentration == 100 / 300


def test_remplir_depasse_capacite():
    # GIVEN
    flacon = Flacon("Sirop de Grenadine", 500)

    # WHEN
    success = flacon.remplir(300, 300)

    # THEN
    assert success is False
    assert flacon.volume == 0
    assert flacon.concentration == 0


def test_transvaser_succes():
    # GIVEN
    flacon_source = Flacon("Sirop de Citron", 500)
    flacon_source.remplir(100, 200)
    flacon_dest = Flacon("Mélange", 500)

    # WHEN
    success = flacon_dest.transvaser(flacon_source, 180)

    # THEN
    assert success is True
    assert flacon_source.volume == 120
    assert flacon_dest.volume == 180


def test_transvaser_volume_insuffisant():
    # GIVEN
    flacon_source = Flacon("Sirop de Citron", 500)
    flacon_dest = Flacon("Mélange", 500)

    # WHEN
    success = flacon_dest.transvaser(flacon_source, 100)

    # THEN
    assert success is False
    assert flacon_source.volume == 0
    assert flacon_dest.volume == 0
