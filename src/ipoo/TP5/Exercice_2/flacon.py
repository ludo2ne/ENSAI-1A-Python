class Flacon:
    """Un flacon de sirop dilué dans de l'eau.

    Attributes
    ----------
    etiquette : str
        L'étiquette du flacon.
    capacite : float
        La capacité du flacon en millilitres.
    volume : float
        Le volume de liquide contenu en millilitres.
    concentration : float
        La concentration en sirop dans le flacon.
    """

    def __init__(self, etiquette, capacite):
        """Constructeur"""
        self.capacite = capacite
        self.etiquette = etiquette
        self.volume = 0
        self.concentration = 0

    def __str__(self) -> str:
        return (
            f"Flacon {self.etiquette}, {self.capacite}mL, "
            f"rempli de {self.volume}mL concentré à {self.concentration:.0%}."
        )

    def remplir(self, volume_sirop, volume_eau) -> bool:
        """Ajoute du sirop et de l'eau dans le flacon si le volume final ne dépasse
        pas la capacité (sinon, l'opération est annulée).

        Parameters
        ----------
        volume_sirop : float
            Volume de sirop en millilitres.
        volume_eau : float
            Volume d'eau en millilitres.

        Returns
        -------
        bool
            True si la capacité n'est pas dépassée.
        """

        if volume_sirop < 0 or volume_eau < 0:
            return False

        nouveau_volume = volume_eau + volume_sirop + self.volume
        if nouveau_volume > self.capacite:
            return False

        self.concentration = (self.volume * self.concentration + volume_sirop) / nouveau_volume
        self.volume = nouveau_volume
        return True

    def transvaser(self, autre_flacon, volume) -> bool:
        """Transvase un certain volume depuis un autre flaon vers le facon courant.
        L'opération est annulée si le volume disponible n'est pas suffisant.

        Mets à jour la concentration dans le flacon courant.

        Parameters
        ----------
        autre_flacon : Flacon
            Le flacon utilisé
        volume : float
            le volume à extraire de autre_flacon

        Returns
        -------
        bool
            True si l'opération a réussi.
        """
        if autre_flacon.volume < volume or self.capacite - self.volume < volume:
            return False

        sirop = volume * autre_flacon.concentration
        eau = volume - sirop

        autre_flacon.volume -= volume
        self.remplir(sirop, eau)

        return True
