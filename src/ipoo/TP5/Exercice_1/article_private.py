class ArticlePrivate:
    """Classe représentant un article"""

    def __init__(self, reference, intitule, prix_ht, quantite_en_stock):
        """Constructeur"""
        self.__reference = reference
        self.__intitule = intitule
        self.__prix_ht = prix_ht
        self.__quantite_en_stock = quantite_en_stock

    def get_reference(self):
        return self.__reference

    def get_intitule(self):
        return self.__intitule

    def get_prix_ht(self):
        return self.__prix_ht

    def get_quantite_en_stock(self):
        return self.__quantite_en_stock

    def __str__(self) -> str:
        return f'#{self.__reference}: "{self.__intitule}", {self.__prix_ht:.2f}€ H.T.'

    def __eq__(self, autre_article) -> bool:
        return self.__reference == autre_article.get_reference()

    def __lt__(self, autre_article) -> bool:
        return self.__quantite_en_stock < autre_article.get_quantite_en_stock()

    def approvisionner(self, nombre_unites) -> None:
        self.__quantite_en_stock += nombre_unites

    def vendre(self, nombre_unites) -> bool:
        if nombre_unites > self.__quantite_en_stock:
            return False
        self.__quantite_en_stock -= nombre_unites
        return True

    def prix_ttc(self) -> float:
        return round(self.__prix_ht * 1.2, 2)
