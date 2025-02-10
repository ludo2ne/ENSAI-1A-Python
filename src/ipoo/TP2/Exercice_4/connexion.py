def connexion(adresse_electronique, mot_de_passe, base_de_donnees):
    """Connexion.

    Parameters
    ----------
    adresse_electronique : str
        Adresse électronique entrée.

    mot_de_passe : str
        Mot de passe entré.

    base_de_donnees : list[tuple[str, str]]
        Base de données représentées sous la forme d'une liste de tuple
        d'adresses électroniques et de mots de passe.
    """
    if (adresse_electronique, mot_de_passe) not in base_de_donnees:
        raise ValueError("Les informations entrées sont erronées.")
