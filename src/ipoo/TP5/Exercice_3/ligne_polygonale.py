from point import Point


class LignePolygonale:
    """Représentation d'une ligne polygonale.

    Attributes
    ----------
    sommets : list[Point]
        La liste de sommets de la ligne polygonale.
    """

    def __init__(self, sommets):
        self.__sommets = sommets
        self.__nb_sommets = len(sommets)

    def __str__(self):
        return " - ".join([str(sommet) for sommet in self.__sommets])

    def get_sommet(self, i) -> "Point":
        """Retourne un des sommets à partir de son index.

        Parameters
        ----------
        i : int
            Index du sommet.

        Returns
        -------
        Point
            Le sommet demandé.
        """
        assert i < self.__nb_sommets

        return self.__sommets[i]

    def set_sommet(self, i, p) -> None:
        """Change un des sommets.

        Parameters
        ----------
        i : int
            Index du sommet à changer.
        p : Point
            Nouveau point.
        """
        assert i < self.__nb_sommets

        self.__sommets[i] = p

    def homothetie(self, k) -> None:
        """Applique une homothétie

        Parameters
        ----------
        k : float
            Rapport d'homothétie.
        """
        for s in self.__sommets:
            s.homothetie(k)

    def translation(self, dx, dy) -> None:
        """Applique une translation

        Parameters
        ----------
        dx : float
            La translation selon l'axe des abscisses.
        dy : float
            La translation selon l'axe des ordonnées.
        """
        for s in self.__sommets:
            s.translation(dx, dy)

    def rotation(self, a) -> None:
        """Applique une rotation par rapport à l'origine.

        Parameters
        ----------
        a : float
            L'angle de rotation.
        """
        for s in self.__sommets:
            s.rotation(a)
