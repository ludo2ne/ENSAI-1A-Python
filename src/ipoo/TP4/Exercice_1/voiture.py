class Voiture:
    """Définition d'une voiture.

    Attributes
    ----------
    nom : str
        Nom de la voiture.
    couleur : str
        Couleur de la voiture.
    vitesse : int (default = 0)
        Vitesse actuelle de la voiture.

    Examples
    --------
    >>> a1 = Voiture('titine', 'bleue')
    >>> a2 = Voiture('quatrelle','verte')
    >>> a3 = Voiture('bovelo','jaune')
    >>> a2.accelere(18)
    >>> a3.accelere(8)
    >>> print(a1)
    Voiture titine de couleur bleue à l'arrêt.
    >>> print(a2)
    Voiture quatrelle de couleur verte roule à 10km/h.
    >>> print(a3)
    Voiture bovelo de couleur jaune roule à 8km/h.
    """

    def __init__(self, nom, couleur, vitesse=0):
        self.couleur = couleur
        self.nom = nom
        self.vitesse = vitesse

    def accelere(self, increment):
        """Augmente la vitesse de la voiture

        Vitesse max = 130km/h, augmentation max = 10km/h.

        Parameters
        ----------
        increment : int
            accélération

        Examples
        ---------
        >>> a1 = Voiture('titine', 'bleue')
        >>> a1.accelere(15)
        >>> print(a1)
        Voiture titine de couleur bleue roule à 10km/h.
        """
        if increment < 0:
            return
        self.vitesse = min(130, self.vitesse + min(increment, 10))

    def freine(self, decrement):
        """Diminue la vitesse de la voiture

        Vitesse min = 0km/h

        Parameters
        ----------
        decrement : int
            décélération

        Examples
        ---------
        >>> a1 = Voiture('titine', 'bleue')
        >>> a1.freine(15)
        >>> print(a1)
        Voiture titine de couleur bleue à l'arrêt.
        """
        if decrement >= 0:
            self.vitesse = max(0, self.vitesse - decrement)

    def est_arretee(self) -> bool:
        """La voiture est-elle à l'arrêt ?

        Returns
        -------
        bool
            True si elle est à 0km/h

        Examples
        ---------
        >>> a1 = Voiture('titine', 'bleue')
        >>> a1.est_arretee()
        True
        """
        return self.vitesse == 0

    def __str__(self):
        """Converti la voiture en chaîne de caractères

        Examples
        ---------
        >>> a1 = Voiture('titine', 'bleue')
        >>> print(a1)
        Voiture titine de couleur bleue à l'arrêt.
        """
        if self.est_arretee():
            v = "à l'arrêt"
        else:
            v = f"roule à {self.vitesse}km/h"

        return f"Voiture {self.nom} de couleur {self.couleur} {v}."


if __name__ == "__main__":
    v1 = Voiture("alice", "jaune")
    print(v1)
