from math import atan2, cos, sin, sqrt


class Point:
    """Construit un point.

    Parameters
    ----------
    x : float
        abscisse du point
    y : float
        ordonnée du point
    """

    def __init__(self, x, y):
        """Constructeur"""
        self.__x = x
        self.__y = y

    def __str__(self) -> str:
        return "({}, {})".format(self.__x, self.__y)

    def __eq__(self, autre_point) -> bool:
        """Teste l'égalité entre deux points.

        Parameters
        ----------
        autre_point : Point
            L'autre point à tester.

        Returns
        -------
        bool
            True si et seulement si les coordonnées correspondent.
        """
        return (self.__x == autre_point.__x) and (self.__y == autre_point.__y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def r(self):
        """Renvoie le rayon en coordonnées polaires."""
        return sqrt(self.__x**2 + self.__y**2)

    @property
    def t(self):
        """Renvoie l'angle en coordonnées polaires"""
        return atan2(self.__y, self.__x)

    def homothetie(self, k):
        """Applique une homothétie au point.

        Parameters
        ----------
        k : float
            Le rapport d'homothétie à appliquer.
        """
        self.__x *= k
        self.__y *= k

    def translation(self, dx, dy):
        """Applique une translation.

        Parameters
        ----------
        dx : float
            La translation selon l'axe des abscisses.
        dy : float
            La translation selon l'axe des ordonnées.
        """
        self.__x += dx
        self.__y += dy

    def rotation(self, a):
        """Applique une rotation par rapport à l'origine.

        Parameters
        ----------
        a : float
            L'angle de rotation.
        """
        t = self.t + a
        self.__x = self.r * cos(t)
        self.__y = self.r * sin(t)
