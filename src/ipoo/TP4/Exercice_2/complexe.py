class Complexe:
    """Nombre complexe.

    Parameters
    ----------
    reel : float
        Partie réelle.
    imaginaire : float
        Partie imaginaire.

    Examples
    --------
    >>> c1 = Complexe(1, 1)
    >>> c2 = Complexe(2, -3)
    >>> print(c1 + c2)
    3 - 2i
    >>> repr(c1 * c2)
    'Complexe(5, -1)'
    """

    def __init__(self, reel, imaginaire):
        self.reel = reel
        self.imaginaire = imaginaire

    def __add__(self, other) -> "Complexe":
        re = self.reel + other.reel
        im = self.imaginaire + other.imaginaire
        return Complexe(re, im)

    def __sub__(self, other) -> "Complexe":
        re = self.reel - other.reel
        im = self.imaginaire - other.imaginaire
        return Complexe(re, im)

    def __mul__(self, other) -> "Complexe":
        return Complexe(
            self.reel * other.reel - self.imaginaire * other.imaginaire,
            self.imaginaire * other.reel + self.reel * other.imaginaire,
        )

    def __str__(self) -> str:
        if self.imaginaire < 0:
            return f"{self.reel} - {-self.imaginaire}i"
        else:
            return f"{self.reel} + {self.imaginaire}i"

    def __repr__(self) -> str:
        return "Complexe({}, {})".format(self.reel, self.imaginaire)


if __name__ == "__main__":
    c1 = Complexe(1, 1)
    c2 = Complexe(2, 2)
    c3 = c1 + c2
    print(c3)

    print(repr(c3))
