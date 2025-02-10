class Domino:
    """Domino d'un jeu de dominos.

    Attributes
    ----------
    extr_A: int (default = 0)
        Extrémité A du domino.

    extr_B: int (default = 0)
        Extrémité B du domino.
    """

    def __init__(self, extr_A=0, extr_B=0):
        self.extr_A = extr_A
        self.extr_B = extr_B

    def __str__(self):
        """Converti le domino en chaîne de caractères

        Returns
        -------
        str

        Examples
        --------
        >>> d1 = Domino(2, 6)
        >>> str(d1)
        '[2|6]'
        """
        return f"[{self.extr_A}|{self.extr_B}]"

    def valeur(self):
        """Retourne la somme des valeurs du domino

        Returns
        -------
        int
            la somme des extrémités

        Examples
        --------
        >>> d1 = Domino(2, 6)
        >>> d1.valeur()
        8
        """
        return self.extr_A + self.extr_B

    def retourne(self):
        """Retourne la somme des valeurs du domino

        Returns
        -------
        int
            la somme des extrémités

        Examples
        --------
        >>> d1 = Domino(2, 6)
        >>> d1.retourne()
        >>> print(d1)
        [6|2]
        """
        self.extr_A, self.extr_B = self.extr_B, self.extr_A

    def accepte_apres(self, other):
        """Vérifie si l'autre domino peut être posé après ce domino.

        Parameters
        ----------
        other : Domino
            Un autre domino.

        Returns
        -------
        bool
            True si l'autre domino peut être posé après ce domino.

        Examples
        --------
        >>> d1 = Domino(2, 6)
        >>> d2 = Domino(4, 3)
        >>> d3 = Domino(6, 3)
        >>> d1.accepte_apres(d2)
        False
        >>> d1.accepte_apres(d3)
        True
        >>> d2.accepte_apres(d3)
        True
        """
        return self.extr_B in (other.extr_A, other.extr_B)
