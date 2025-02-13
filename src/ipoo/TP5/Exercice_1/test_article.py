import pytest
from article import Article


def test_str():
    # GIVEN
    article = Article(123, "pomme", 0.40, 12)

    # WHEN
    result = str(article)

    # THEN
    assert result == '#123: "pomme", 0.40€ H.T.'


def test_egalite_true():
    # GIVEN
    article1 = Article(123, "pomme", 0.40, 12)
    article3 = Article(123, "pomme", 0.45, 6)

    # WHEN
    equality = article1 == article3

    # THEN
    assert equality is True


def test_egalite_false():
    # GIVEN
    article1 = Article(123, "pomme", 0.40, 12)
    article2 = Article(126, "poire", 0.30, 9)

    # WHEN
    equality = article1 == article2

    # THEN
    assert equality is False


def test_stock_lower_than_true():
    # GIVEN
    article1 = Article(123, "pomme", 0.40, 12)
    article2 = Article(126, "poire", 0.30, 50)

    # WHEN
    res = article1 < article2

    # THEN
    assert res is True


def test_stock_lower_than_false():
    # GIVEN
    article1 = Article(123, "pomme", 0.40, 12)
    article2 = Article(126, "poire", 0.30, 9)

    # WHEN
    result1 = article1 < article2

    # THEN
    assert result1 is False


def test_approvisionner():
    # GIVEN
    article = Article(123, "pomme", 0.40, 12)

    # WHEN
    article.approvisionner(3)

    # THEN
    assert article.quantite_en_stock == 15


def test_vendre_stock_suffisant():
    # GIVEN
    article = Article(123, "pomme", 0.40, 12)

    # WHEN
    res = article.vendre(5)

    # THEN
    assert res is True
    assert article.quantite_en_stock == 7


def test_vendre_stock_insuffisant():
    # GIVEN
    article = Article(123, "pomme", 0.40, 12)

    # WHEN
    res = article.vendre(30)

    # THEN
    assert res is False
    assert article.quantite_en_stock == 12


def test_prix_ttc():
    # GIVEN
    article = Article(123, "pomme", 0.40, 12)

    # WHEN
    result = article.prix_ttc()

    # THEN
    assert result == 0.48


if __name__ == "__main__":
    pytest.main()
