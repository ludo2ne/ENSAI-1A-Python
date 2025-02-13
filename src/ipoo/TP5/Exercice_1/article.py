class Article:
    """Classe représentant un article

    Attributes
    ----------
    reference : int
        référence de l'article
    intitule : str
        intitulé de l'article
    prix_ht : float
        prix hors taxes
    quantite_en_stock : int
        nombre d'unités disponibles

    Examples
    --------
    >>> article1 = Article(123, "pomme", 0.40, 12)
    >>> article2 = Article(126, "poire", 0.30, 8)
    >>> article1 == article2
    False
    >>> article2 < article1
    True
    >>> article2.approvisionner(8)
    >>> article1 < article2
    True
    >>> article2.vendre(20)
    False
    >>> article2.vendre(6)
    True
    >>> article2 < article1
    True
    """

    def __init__(self, reference, intitule, prix_ht, quantite_en_stock):
        """Constructeur"""
        self.reference = reference
        self.intitule = intitule
        self.prix_ht = prix_ht
        self.quantite_en_stock = quantite_en_stock

    def __str__(self) -> str:
        """
        Examples
        --------
        >>> article1 = Article(123, "pomme", 0.40, 12)
        >>> print(article1)
        #123: "pomme", 0.40€ H.T.
        """
        return f'#{self.reference}: "{self.intitule}", {self.prix_ht:.2f}€ H.T.'

    def __eq__(self, autre_article) -> bool:
        """Test d'égalité entre deux articles.

        Parameters
        ----------
        autre_article : Article
            Article dont il faut tester l'égalité

        Returns
        -------
        bool
            True si ce sont les même articles

        Examples
        --------
        >>> article1 = Article(123, "pomme", 0.40, 12)
        >>> article2 = Article(126, "poire", 0.30, 9)
        >>> article3 = Article(123, "pomme", 0.45, 6)
        >>> article1 == article2
        False
        >>> article1 == article3
        True
        """
        return self.reference == autre_article.reference

    def __lt__(self, autre_article) -> bool:
        """Comparaison de stock avec un autre article.

        Parameters
        ----------
        autre_article : Article
            L'article à comparer

        Returns
        -------
        bool
            True si le stock courant est strictement inférieur

        Examples
        --------
        >>> article1 = Article(123, "pomme", 0.40, 12)
        >>> article2 = Article(126, "poire", 0.30, 9)
        >>> article2 < article1
        True
        """
        return self.quantite_en_stock < autre_article.quantite_en_stock

    def approvisionner(self, nombre_unites) -> None:
        """Augmente le stock de l'article.

        Parameters
        ----------
        nombre_unites : int
            La quantité à ajouter

        Examples
        --------
        >>> article = Article(123, "pomme", 0.40, 12)
        >>> article.approvisionner(2)
        >>> article.quantite_en_stock
        14
        """
        self.quantite_en_stock += nombre_unites

    def vendre(self, nombre_unites) -> bool:
        """Diminue le stock du nombre d'unités vendues.

        Parameters
        ----------
        nombre_unites : int
            La quantité que l'on souhaite vendre

        Returns
        -------
        bool
            True si le stock était suffisant pour la vente.

        Examples
        --------
        >>> article = Article(123, "pomme", 0.40, 12)
        >>> article.vendre(20)
        False
        >>> article.vendre(8)
        True
        >>> article.quantite_en_stock
        4
        """
        if nombre_unites > self.quantite_en_stock:
            return False
        self.quantite_en_stock -= nombre_unites
        return True

    def prix_ttc(self) -> float:
        """Calcule le prix Toutes Taxes Comprises.

        Returns
        -------
        float
            Le prix TTC arrondi à 2 chiffres après la virgule.

        Examples
        --------
        >>> article = Article(123, "pomme", 0.40, 12)
        >>> article.prix_ttc()
        0.48
        """
        return round(self.prix_ht * 1.2, 2)
